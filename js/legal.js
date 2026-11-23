/* Language selector + page rendering for ViewWeave legal pages. Default: English. */
(function () {
  const STORAGE_KEY = "vw_legal_lang";
  const DEFAULT_LANG = "en";

  function pageKind() {
    const path = (location.pathname.split("/").pop() || "index.html").toLowerCase();
    if (path.startsWith("privacy")) return "privacy";
    if (path.startsWith("support")) return "support";
    return "index";
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
    const u = new URL(href, location.href);
    if (lang === DEFAULT_LANG) u.searchParams.delete("lang");
    else u.searchParams.set("lang", lang);
    return u.pathname.split("/").pop() + u.search + u.hash;
  }

  function applyChrome(pack, lang) {
    const ui = pack.ui || {};
    const kind = pageKind();
    if (kind === "privacy" && pack.privacy && pack.privacy.h1) {
      document.title = "ViewWeave — " + pack.privacy.h1;
    } else if (kind === "support" && pack.support && pack.support.h1) {
      document.title = "ViewWeave — " + pack.support.h1;
    } else if (ui.index_h1) {
      document.title = "ViewWeave — " + ui.index_h1;
    }

    setText("lang-label", ui.lang_label || "Language");
    setText("nav-home", ui.nav_home || "Home");
    setText("nav-support", ui.nav_support || "Support");
    setText("nav-privacy", ui.nav_privacy || "Privacy Policy");
    setText("footer-copy", ui.footer_copy || "© 2026 ViewWeave");
    setText("footer-support", ui.nav_support || "Support");
    setText("footer-privacy", ui.nav_privacy || "Privacy Policy");

    document.querySelectorAll("a[href]").forEach((a) => {
      const raw = a.getAttribute("href");
      if (!raw || raw.startsWith("mailto:") || raw.startsWith("http")) return;
      if (!/^(index|privacy|support)\.html/.test(raw.split("?")[0])) return;
      a.setAttribute("href", withLang(raw.split("?")[0], lang));
    });
  }

  function applyIndex(pack) {
    const ui = pack.ui || {};
    const idx = pack.index || {};
    setText("page-tag", idx.tag || "");
    setText("index-h1", ui.index_h1 || "");
    setText("index-lead", ui.index_lead || "");
    setText("index-support-strong", ui.index_support_strong || "Support:");
    setText("index-privacy-strong", ui.index_privacy_strong || "Privacy:");
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

  function apply(lang) {
    const pack = t(lang);
    fillLangSelect(lang);
    applyChrome(pack, lang);
    const kind = pageKind();
    if (kind === "privacy") applyPrivacy(pack);
    else if (kind === "support") applySupport(pack);
    else applyIndex(pack);
    document.documentElement.lang =
      lang === "pt_BR" ? "pt-BR" : lang === "zh_TW" ? "zh-Hant" : lang;
  }

  document.addEventListener("DOMContentLoaded", () => {
    apply(resolveLang());
  });
})();
