/* Language selector + page rendering for ViewWeave legal pages. Default: English. */
(function () {
  const STORAGE_KEY = "vw_legal_lang";
  const DEFAULT_LANG = "en";

  function pageKind() {
    const path = location.pathname.replace(/\\/g, "/");
    if (/\/guide(\/index\.html)?$/i.test(path) || /\/guide\/$/i.test(path)) {
      return "guide";
    }
    const leaf = (path.split("/").pop() || "index.html").toLowerCase();
    if (leaf.startsWith("privacy")) return "privacy";
    if (leaf.startsWith("support")) return "support";
    if (leaf.startsWith("guide")) return "guide";
    return "index";
  }

  function inGuideDir() {
    return pageKind() === "guide";
  }

  function availableIds() {
    return (window.VW_LEGAL_LOCALES || []).map((l) => l.id);
  }

  function resolveLang() {
    const params = new URLSearchParams(location.search);
    const fromQuery = params.get("lang");
    const ids = availableIds();
    if (fromQuery && ids.includes(fromQuery)) return fromQuery;
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored && ids.includes(stored)) return stored;
    } catch (_) {}
    return DEFAULT_LANG;
  }

  function setLang(lang) {
    const ids = availableIds();
    const next = ids.includes(lang) ? lang : DEFAULT_LANG;
    try {
      localStorage.setItem(STORAGE_KEY, next);
    } catch (_) {}
    const url = new URL(location.href);
    if (next === DEFAULT_LANG) url.searchParams.delete("lang");
    else url.searchParams.set("lang", next);
    history.replaceState(null, "", url);
    apply(next);
  }

  function t(lang) {
    const all = window.VW_LEGAL_I18N || {};
    return all[lang] || all[DEFAULT_LANG] || {};
  }

  function guidePack(lang) {
    const all = window.VW_GUIDE_I18N || {};
    return all[lang] || all[DEFAULT_LANG] || {};
  }

  function fillLangSelect(lang) {
    const sel = document.getElementById("lang-select");
    if (!sel) return;
    const locales = window.VW_LEGAL_LOCALES || [];
    sel.innerHTML = "";
    for (const loc of locales) {
      const opt = document.createElement("option");
      opt.value = loc.id;
      opt.textContent = loc.label;
      if (loc.id === lang) opt.selected = true;
      sel.appendChild(opt);
    }
    sel.onchange = () => setLang(sel.value);
  }

  function setHtml(id, html) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = html == null ? "" : html;
  }

  function setText(id, text) {
    const el = document.getElementById(id);
    if (el) el.textContent = text == null ? "" : text;
  }

  function withLang(href, lang) {
    if (!href) return href;
    const pathOnly = href.split("?")[0].split("#")[0];
    const hashIdx = href.indexOf("#");
    const hash = hashIdx >= 0 ? href.slice(hashIdx) : "";
    if (lang === DEFAULT_LANG) return pathOnly + hash;
    return pathOnly + "?lang=" + encodeURIComponent(lang) + hash;
  }

  function rewriteNavLinks(lang) {
    document.querySelectorAll("a[href]").forEach((a) => {
      const raw = a.getAttribute("href");
      if (!raw || raw.startsWith("mailto:") || raw.startsWith("http")) return;
      const pathOnly = raw.split("?")[0].split("#")[0];
      if (
        !/(^|\/)(index|privacy|support)\.html$/.test(pathOnly) &&
        !/(^|\/)guide\/index\.html$/.test(pathOnly)
      ) {
        return;
      }
      a.setAttribute("href", withLang(pathOnly, lang));
    });
  }

  const HEADER_LOCALES = {
    en: "en",
    de: "de",
    el: "el",
    es: "es",
    fr: "fr",
    it: "it",
    ja: "ja",
    ko: "ko",
    nl: "nl",
    pl: "pl",
    pt: "pt",
    pt_BR: "pt_BR",
    tr: "tr",
    zh: "zh",
    // Fallbacks when no dedicated store header asset exists
    th: "en",
    zh_TW: "zh",
  };

  function headerAssetLang(lang) {
    return HEADER_LOCALES[lang] || "en";
  }

  function applyStoreBanner(lang) {
    const img = document.getElementById("store-banner-img");
    if (!img) return;
    const code = headerAssetLang(lang);
    const file = "asc_header_" + code + "_3840x1646.jpg";
    const base = inGuideDir() ? "../headers/" : "headers/";
    const next = base + file;
    if (img.getAttribute("src") !== next) img.setAttribute("src", next);
  }

  function applyChrome(pack, lang, guide) {
    const ui = pack.ui || {};
    const kind = pageKind();
    if (kind === "guide" && guide && guide.h1) {
      document.title = "ViewWeave — " + guide.h1;
    } else if (kind === "privacy" && pack.privacy && pack.privacy.h1) {
      document.title = "ViewWeave — " + pack.privacy.h1;
    } else if (kind === "support" && pack.support && pack.support.h1) {
      document.title = "ViewWeave — " + pack.support.h1;
    } else if (ui.index_h1) {
      document.title = "ViewWeave — " + ui.index_h1;
    }

    applyStoreBanner(lang);

    setText("lang-label", ui.lang_label || "Language");
    setText("nav-home", ui.nav_home || "Home");
    setText("nav-support", ui.nav_support || "Support");
    setText("nav-privacy", ui.nav_privacy || "Privacy Policy");
    setText("nav-guide", ui.nav_guide || "Guide");
    setText("footer-copy", ui.footer_copy || "© 2026 ViewWeave");
    setText("footer-support", ui.nav_support || "Support");
    setText("footer-privacy", ui.nav_privacy || "Privacy Policy");
    setText("footer-guide", ui.nav_guide || "Guide");
    setText("index-guide-strong", ui.index_guide_strong || "Guide:");

    rewriteNavLinks(lang);
  }

  function applyIndex(pack) {
    const ui = pack.ui || {};
    const idx = pack.index || {};
    setText("page-tag", idx.tag || "");
    setText("index-h1", ui.index_h1 || "");
    setText("index-lead", ui.index_lead || "");
    setText("index-support-strong", ui.index_support_strong || "Support:");
    setText("index-privacy-strong", ui.index_privacy_strong || "Privacy:");
    setText("index-guide-strong", ui.index_guide_strong || "Guide:");
  }

  function applyPrivacy(pack) {
    const p = pack.privacy || {};
    setText("page-tag", p.tag || "");
    setText("privacy-h1", p.h1 || "");
    setText("privacy-effective", p.effective || "");
    setHtml("privacy-intro", p.intro);
    setText("privacy-h2-1", p.h2_1 || "");
    setHtml("privacy-p-1", p.p_1);
    setText("privacy-h2-2", p.h2_2 || "");
    setHtml("privacy-li-2a", p.li_2a);
    setHtml("privacy-li-2b", p.li_2b);
    setHtml("privacy-li-2c", p.li_2c);
    setText("privacy-p-2", p.p_2 || "");
    setText("privacy-h2-3", p.h2_3 || "");
    setHtml("privacy-p-3", p.p_3);
    setText("privacy-h2-4", p.h2_4 || "");
    setHtml("privacy-p-4", p.p_4);
    setText("privacy-h2-5", p.h2_5 || "");
    setHtml("privacy-li-5a", p.li_5a);
    setHtml("privacy-li-5b", p.li_5b);
    setHtml("privacy-li-5c", p.li_5c);
    setHtml("privacy-li-5d", p.li_5d);
    setText("privacy-h2-6", p.h2_6 || "");
    setText("privacy-p-6", p.p_6 || "");
    setText("privacy-h2-7", p.h2_7 || "");
    setHtml("privacy-li-7a", p.li_7a);
    setHtml("privacy-li-7b", p.li_7b);
    setHtml("privacy-li-7c", p.li_7c);
    setHtml("privacy-li-7d", p.li_7d);
    setText("privacy-h2-8", p.h2_8 || "");
    setText("privacy-p-8", p.p_8 || "");
  }

  function applySupport(pack) {
    const s = pack.support || {};
    setText("page-tag", s.tag || "");
    setText("support-h1", s.h1 || "");
    setHtml("support-intro", s.intro);
    setText("support-contact", s.contact || "");
    setText("support-h2", s.h2 || "");
    setHtml("support-li-a", s.li_a);
    setHtml("support-li-b", s.li_b);
    setHtml("support-li-c", s.li_c);
    setHtml("support-li-d", s.li_d);
  }

  function videoSrc(file) {
    // Videos live in docs/legal/ (parent of guide/)
    return inGuideDir() ? "../" + file : file;
  }

  function thumbSrc(file) {
    const base = String(file || "").replace(/\.MP4$/i, ".jpg");
    return inGuideDir() ? "../thumbs/" + base : "thumbs/" + base;
  }

  function ensureVideoModal() {
    const modal = document.getElementById("video-modal");
    if (!modal || modal.dataset.bound === "1") return modal;
    modal.dataset.bound = "1";
    const player = document.getElementById("video-modal-player");

    function closeModal() {
      modal.hidden = true;
      document.body.style.overflow = "";
      if (player) {
        player.pause();
        player.removeAttribute("src");
        player.load();
      }
    }

    modal.querySelectorAll("[data-close-modal]").forEach((el) => {
      el.addEventListener("click", closeModal);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !modal.hidden) closeModal();
    });
    modal._close = closeModal;
    return modal;
  }

  function openVideoModal(title, file) {
    const modal = ensureVideoModal();
    const player = document.getElementById("video-modal-player");
    const titleEl = document.getElementById("video-modal-title");
    if (!modal || !player) return;
    if (titleEl) titleEl.textContent = title || file;
    player.src = videoSrc(file);
    modal.hidden = false;
    document.body.style.overflow = "hidden";
    player.play().catch(() => {});
  }

  const GUIDE_SHOT_LOCALES = {
    en: 1,
    de: 1,
    el: 1,
    es: 1,
    fr: 1,
    it: 1,
    ja: 1,
    ko: 1,
    nl: 1,
    pl: 1,
    pt: 1,
    pt_BR: 1,
    th: 1,
    tr: 1,
    zh: 1,
    zh_TW: 1,
  };

  function guideShotLang(lang) {
    return GUIDE_SHOT_LOCALES[lang] ? lang : "en";
  }

  function localizeGuideHtml(html, lang) {
    const code = guideShotLang(lang);
    return String(html || "").replace(/assets\/__LANG__\//g, "assets/" + code + "/");
  }

  function applyGuide(g, lang) {
    setText("page-tag", g.tag || "");
    setText("guide-h1", g.h1 || "");
    setText("guide-lead", g.lead || "");
    setText("guide-videos-h2", g.videos_h2 || "");

    ensureVideoModal();

    const vidHost = document.getElementById("guide-videos");
    if (vidHost) {
      vidHost.innerHTML = "";
      (g.videos || []).forEach((v) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "video-thumb";
        btn.setAttribute("aria-label", v.title || v.file);

        const media = document.createElement("div");
        media.className = "video-thumb-media";
        const img = document.createElement("img");
        img.src = thumbSrc(v.file);
        img.alt = "";
        img.loading = "lazy";
        img.width = 120;
        img.height = 213;
        const play = document.createElement("div");
        play.className = "video-thumb-play";
        play.setAttribute("aria-hidden", "true");
        media.appendChild(img);
        media.appendChild(play);

        const h = document.createElement("h3");
        h.textContent = v.title || v.file;

        btn.appendChild(media);
        btn.appendChild(h);
        btn.addEventListener("click", () => openVideoModal(v.title || v.file, v.file));
        vidHost.appendChild(btn);
      });
    }

    const toc = document.getElementById("guide-toc");
    if (toc) {
      const title = g.toc_h2 || "Contents";
      const ol = document.createElement("ol");
      (g.sections || []).forEach((s) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = "#" + s.id;
        a.textContent = s.title;
        li.appendChild(a);
        ol.appendChild(li);
      });
      toc.innerHTML = "";
      const h = document.createElement("h2");
      h.textContent = title;
      toc.appendChild(h);
      toc.appendChild(ol);
    }

    const body = document.getElementById("guide-body");
    if (body) {
      body.innerHTML = "";
      (g.sections || []).forEach((s) => {
        const sec = document.createElement("section");
        sec.id = s.id;
        const h2 = document.createElement("h2");
        h2.textContent = s.title;
        sec.appendChild(h2);
        const wrap = document.createElement("div");
        wrap.innerHTML = localizeGuideHtml(s.html || "", lang);
        while (wrap.firstChild) sec.appendChild(wrap.firstChild);
        body.appendChild(sec);
      });
    }
  }

  function apply(lang) {
    const pack = t(lang);
    const guide = guidePack(lang);
    fillLangSelect(lang);
    applyChrome(pack, lang, guide);
    const kind = pageKind();
    if (kind === "privacy") applyPrivacy(pack);
    else if (kind === "support") applySupport(pack);
    else if (kind === "guide") applyGuide(guide, lang);
    else applyIndex(pack);
    document.documentElement.lang =
      lang === "pt_BR" ? "pt-BR" : lang === "zh_TW" ? "zh-Hant" : lang;
  }

  document.addEventListener("DOMContentLoaded", () => {
    apply(resolveLang());
  });
})();
