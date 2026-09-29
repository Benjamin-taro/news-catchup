// 👍/👎 ボタン：押すと GitHub 上の Digest の Markdown（`- [ ] 👍` / `- [ ] 👎`）を直接書き換える。
// トークンはこのブラウザの localStorage にだけ保存する。トークンがない端末ではボタンを出さない。
(() => {
  const REPO = "Benjamin-taro/news-catchup";
  const BRANCH = "main";
  const KEY = "news-catchup:gh-token";
  const API = `https://api.github.com/repos/${REPO}`;
  const script = document.currentScript;

  const getToken = () => { try { return localStorage.getItem(KEY) || ""; } catch { return ""; } };
  const setToken = (t) => { try { t ? localStorage.setItem(KEY, t) : localStorage.removeItem(KEY); return true; } catch { return false; } };

  const headers = (token) => ({
    Authorization: `Bearer ${token}`,
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
  });

  function toast(msg) {
    const el = document.createElement("div");
    el.className = "vote-toast";
    el.setAttribute("role", "status");
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 2600);
  }

  const b64decode = (b64) => {
    const bin = atob(b64.replace(/\n/g, ""));
    return new TextDecoder().decode(Uint8Array.from(bin, (c) => c.charCodeAt(0)));
  };
  const b64encode = (text) => {
    const bytes = new TextEncoder().encode(text);
    let bin = "";
    for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
    return btoa(bin);
  };

  // Markdown から、記事番号ごとの 👍/👎 行の位置と状態を取り出す
  const VOTE_LINE = /^([-*]\s*\[)( |x|X)(\]\s*)(👍|👎)/;
  function parseVotes(lines) {
    const votes = {};
    let rank = null;
    lines.forEach((line, i) => {
      const h = line.match(/^## (\d+)\. /);
      if (h) { rank = h[1]; return; }
      if (line.startsWith("## ")) { rank = null; return; }
      const v = rank && line.match(VOTE_LINE);
      if (v) (votes[rank] ||= {})[v[4]] = { line: i, on: v[2] !== " " };
    });
    return votes;
  }

  async function fetchFile(path, token) {
    const res = await fetch(`${API}/contents/${encodeURI(path)}?ref=${BRANCH}`, { headers: headers(token), cache: "no-store" });
    if (!res.ok) throw new Error(`GET ${res.status}`);
    const json = await res.json();
    return { sha: json.sha, text: b64decode(json.content) };
  }

  function render(votes) {
    document.querySelectorAll(".vote-bar").forEach((bar) => {
      const v = votes[bar.dataset.rank];
      if (!v) { bar.hidden = true; return; }
      bar.hidden = false;
      bar.querySelectorAll(".vote-btn").forEach((btn) => {
        btn.setAttribute("aria-pressed", String(!!(v[btn.dataset.vote] && v[btn.dataset.vote].on)));
      });
    });
  }

  async function initDigest(path) {
    const token = getToken();
    if (!token) return;
    let votes;
    try {
      votes = parseVotes((await fetchFile(path, token)).text.split("\n"));
    } catch (e) {
      toast(`👍/👎 の状態を読み込めませんでした（${e.message}）`);
      return;
    }
    render(votes);

    document.addEventListener("click", async (ev) => {
      const btn = ev.target.closest(".vote-btn");
      const bar = btn && btn.closest(".vote-bar");
      if (!bar) return;
      const rank = bar.dataset.rank;
      const kind = btn.dataset.vote;
      const turnOn = btn.getAttribute("aria-pressed") !== "true";
      bar.querySelectorAll(".vote-btn").forEach((b) => (b.disabled = true));
      try {
        for (let attempt = 0; attempt < 2; attempt++) {
          const { sha, text } = await fetchFile(path, token);
          const lines = text.split("\n");
          const v = parseVotes(lines)[rank];
          if (!v || !v[kind]) throw new Error("この記事にはチェック欄がありません");
          const set = (k, on) => { if (v[k]) lines[v[k].line] = lines[v[k].line].replace(VOTE_LINE, (_, a, _c, b, e) => `${a}${on ? "x" : " "}${b}${e}`); };
          set(kind, turnOn);
          if (turnOn) set(kind === "👍" ? "👎" : "👍", false); // 👍 と 👎 は片方だけ
          const res = await fetch(`${API}/contents/${encodeURI(path)}`, {
            method: "PUT",
            headers: { ...headers(token), "Content-Type": "application/json" },
            body: JSON.stringify({
              message: `Vote ${turnOn ? kind : "clear " + kind} #${rank} ${path.replace(/^Digest\/|\.md$/g, "")}`,
              content: b64encode(lines.join("\n")),
              sha,
              branch: BRANCH,
            }),
          });
          if (res.ok) {
            render(parseVotes(lines));
            toast(turnOn ? `${kind} を記録しました` : `${kind} を取り消しました`);
            return;
          }
          if (res.status !== 409 && res.status !== 422) throw new Error(`PUT ${res.status}`);
          // ほかの更新と衝突したら、最新を取り直してもう一度
        }
        throw new Error("更新が衝突しました。少し待ってから押し直してください");
      } catch (e) {
        toast(`記録できませんでした：${e.message}`);
      } finally {
        bar.querySelectorAll(".vote-btn").forEach((b) => (b.disabled = false));
      }
    });
  }

  function initSettings() {
    const form = document.getElementById("token-form");
    const input = document.getElementById("token-input");
    const status = document.getElementById("token-status");
    const show = (msg) => (status.textContent = msg);
    show(getToken() ? "この端末にはトークンが登録されています。" : "まだ登録されていません。");

    form.addEventListener("submit", async (ev) => {
      ev.preventDefault();
      const token = input.value.trim();
      if (!token) return show("トークンを入力してください。");
      show("確認中…");
      try {
        const res = await fetch(API, { headers: headers(token) });
        if (!res.ok) throw new Error(`GitHub が ${res.status} を返しました`);
        const repo = await res.json();
        if (!(repo.permissions && repo.permissions.push)) throw new Error("このリポジトリへの書き込み権限がありません（Contents: Read and write を確認）");
        if (!setToken(token)) throw new Error("このブラウザでは保存できませんでした（プライベートモードなど）");
        input.value = "";
        show("✅ 登録しました。各日のページに 👍/👎 ボタンが表示されます。");
      } catch (e) {
        show(`❌ ${e.message}`);
      }
    });
    document.getElementById("token-clear").addEventListener("click", () => {
      setToken("");
      show("この端末からトークンを削除しました。");
    });
  }

  if (script.dataset.settings) initSettings();
  else if (script.dataset.digest) initDigest(script.dataset.digest);
})();
