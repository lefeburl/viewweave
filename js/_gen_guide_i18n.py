#!/usr/bin/env python3
"""Generate docs/legal/js/guide_i18n.js — user guide in all app languages."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).with_name("guide_i18n.js")
EN_FR = Path(__file__).with_name("_guide_en_fr.json")
EXTRA = Path(__file__).with_name("_guide_extra.json")

LOCALES = [
    "en", "de", "el", "es", "fr", "it", "ja", "ko",
    "nl", "pl", "pt", "pt_BR", "th", "tr", "zh", "zh_TW",
]


def img(src: str, alt: str) -> str:
    # __LANG__ is rewritten at runtime by legal.js to the active locale (fallback en).
    return (
        f'<img class="guide-shot" src="assets/__LANG__/{src}" '
        f'alt="{alt}" loading="lazy" />'
    )


def table(headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows
    )
    return (
        f'<table class="guide-table"><thead><tr>{th}</tr></thead>'
        f"<tbody>{body}</tbody></table>"
    )


def pre(text: str) -> str:
    return f'<pre class="guide-pre">{text}</pre>'


def callout(html: str) -> str:
    return f'<p class="guide-callout">{html}</p>'


def section(sid: str, title: str, html: str) -> dict:
    return {"id": sid, "title": title, "html": html}


def build_from_strings(S: dict) -> dict:
    """Build a full guide pack from a flat string map (shared structure)."""
    videos = [
        {"file": "01_INTRO.MP4", "title": S["v1"]},
        {"file": "02_CREATE_MASTER.MP4", "title": S["v2"]},
        {"file": "03_CREATE_SLAVE_2ND_PHONE.MP4", "title": S["v3"]},
        {"file": "04_CALIBRATION_RECORDING.MP4", "title": S["v4"]},
        {"file": "05_2ND_PHONE_AUTORECORD.MP4", "title": S["v5"]},
        {"file": "06_MOUNTING.MP4", "title": S["v6"]},
    ]
    sections = [
        section(
            "s1",
            S["s1_t"],
            f"<p>{S['s1_p']}</p>" + pre(S["s1_pre"]),
        ),
        section(
            "s2",
            S["s2_t"],
            table(
                [S["h_term"], S["h_meaning"], S["h_example"]],
                [
                    [f"<strong>{S['term_session']}</strong>", S["def_session"], S["ex_session"]],
                    [f"<strong>{S['term_take']}</strong>", S["def_take"], S["ex_take"]],
                    [f"<strong>{S['term_angle']}</strong>", S["def_angle"], S["ex_angle"]],
                    [f"<strong>{S['term_segment']}</strong>", S["def_segment"], S["ex_segment"]],
                    [f"<strong>{S['term_rush']}</strong>", S["def_rush"], S["ex_rush"]],
                ],
            )
            + pre(S["s2_pre"])
            + callout(S["s2_note"]),
        ),
        section(
            "s3",
            S["s3_t"],
            img("01_home.png", S["alt_home"])
            + table(
                [S["h_item"], S["h_role"], S["h_when"]],
                [
                    [f"<strong>{S['master']}</strong>", S["master_role"], S["master_when"]],
                    [f"<strong>{S['camera']}</strong>", S["camera_role"], S["camera_when"]],
                    [f"<strong>{S['library']}</strong>", S["library_role"], S["library_when"]],
                    [f"<strong>Basic / Free</strong>", S["license_role"], S["license_when"]],
                    [f"<strong>{S['replay']}</strong>", S["replay_role"], S["replay_when"]],
                ],
            )
            + f"<h3>{S['s3_create']}</h3>"
            + img("02_create.png", S["alt_new"])
            + table(
                [S["h_control"], S["h_role"], S["h_usecase"]],
                [
                    [f"<strong>{S['new']}</strong>", S["new_role"], S["new_use"]],
                    [f"<strong>{S['existing']}</strong>", S["existing_role"], S["existing_use"]],
                    [f"<strong>{S['session_name']}</strong>", S["session_name_role"], S["session_name_use"]],
                    [f"<strong>{S['classic']}</strong>", S["classic_role"], S["classic_use"]],
                    [f"<strong>{S['instant']}</strong>", S["instant_role"], S["instant_use"]],
                    [f"<strong>{S['continue']}</strong>", S["continue_role"], S["continue_use"]],
                ],
            )
            + callout(S["s3_note"])
            + f"<h3>{S['s3_join']}</h3>"
            + img("04_join.png", S["alt_join"])
            + table(
                [S["h_action"], S["h_role"], S["h_usecase"]],
                [
                    [f"<strong>{S['hotspot']}</strong> <em>(Android)</em>", S["hotspot_role"], S["hotspot_use"]],
                    [f"<strong>{S['scan_qr']}</strong>", S["scan_qr_role"], S["scan_qr_use"]],
                    [f"<strong>{S['ip_link']}</strong> + <strong>{S['join']}</strong>", S["ip_link_role"], S["ip_link_use"]],
                ],
            )
            + f"<p>{S['same_network']}</p>",
        ),
        section(
            "s4",
            S["s4_t"],
            table(
                ["", f"<strong>{S['classic']}</strong>", f"<strong>{S['instant']}</strong>"],
                [
                    [f"<strong>{S['master_btn']}</strong>", S["classic_btn"], S["instant_btn"]],
                    [f"<strong>{S['trigger']}</strong>", S["classic_trigger"], S["instant_trigger"]],
                    [f"<strong>{S['filters']}</strong>", S["classic_filters"], S["instant_filters"]],
                    [f"<strong>{S['resolution']}</strong>", S["classic_res"], S["instant_res"]],
                    [f"<strong>{S['during_xfer']}</strong>", S["classic_xfer"], S["instant_xfer"]],
                    [f"<strong>{S['best_for']}</strong>", S["classic_best"], S["instant_best"]],
                ],
            ),
        ),
        section(
            "s5",
            S["s5_t"],
            img("03_waiting.png", S["alt_waiting"])
            + f"<p>{S['s5_p']}</p>"
            + table(
                [S["h_control"], S["h_role"], S["h_usecase"]],
                [
                    [f"<strong>{S['hotspot']}</strong> <em>(Android)</em>", S["hotspot_role"], S["hotspot_use"]],
                    [f"<strong>{S['master_ip']}</strong> + <strong>{S['refresh_ip']}</strong>", S["master_ip_role"], S["master_ip_use"]],
                    [f"<strong>{S['copy_link']}</strong>", S["copy_link_role"], S["copy_link_use"]],
                    [f"<strong>QR</strong>", S["qr_role"], S["qr_use"]],
                    [f"<strong>{S['device_list']}</strong>", S["device_list_role"], S["device_list_use"]],
                    [f"<strong>{S['comp_capture']}</strong> <em>(Basic+)</em>", S["comp_capture_role"], S["comp_capture_use"]],
                    [f"<strong>{S['calibrate']}</strong>", S["calibrate_role"], S["calibrate_use"]],
                    [f"<strong>{S['film_uncal']}</strong> / <strong>{S['film']}</strong>", S["film_role"], S["film_use"]],
                    [f"<strong>{S['library']}</strong>", S["lib_leave_role"], S["lib_leave_use"]],
                ],
            ),
        ),
        section(
            "s6",
            S["s6_t"],
            f"<h3>{S['s6_master']}</h3>"
            + table(
                [S["h_control"], S["h_who"], S["h_role"]],
                [
                    [f"<strong>Rec / Stop</strong>", f"<strong>{S['master_only']}</strong>", S["rec_role"]],
                    [f"<strong>Instant / mark</strong>", f"<strong>{S['master_only']}</strong>", S["mark_role"]],
                    [f"<strong>{S['n_cams']}</strong>", S["master"], S["n_cams_role"]],
                    [f"<strong>EXPO / FILTER / NIGHT / …</strong>", S["both"], S["local_role"]],
                ],
            )
            + f"<h3>{S['s6_slave']}</h3>"
            + table(
                [S["h_indicator"], S["h_role"]],
                [
                    [S["slave_msg"], S["slave_msg_role"]],
                    [S["waiting_rec"], S["session_state"]],
                    [S["local_controls"], S["local_this_cam"]],
                    [S["back"], S["leave_session"]],
                ],
            )
            + table(
                [S["h_action"], S["master"], "Slave"],
                [
                    [S["act_create"], "✅", "❌"],
                    [S["act_rec"], "✅", S["act_rec_slave"]],
                    [S["act_local"], "✅", "✅"],
                    [S["act_receive"], "✅", S["act_receive_slave"]],
                    [S["act_edit"], "✅", S["act_edit_slave"]],
                ],
            ),
        ),
        section(
            "s7",
            S["s7_t"],
            f"<ol><li>{S['s7_1']}</li><li>{S['s7_2']}</li><li>{S['s7_3']}</li><li>{S['s7_4']}</li></ol>"
            + table(
                [S["h_case"], S["h_behaviour"]],
                [
                    [S["classic"], S["xfer_classic"]],
                    [S["instant"], S["xfer_instant"]],
                    [S["slave_disc"], S["xfer_disc"]],
                ],
            ),
        ),
        section(
            "s8",
            S["s8_t"],
            img("05_library.png", S["alt_lib"])
            + table(
                [S["h_action"], S["h_role"], S["h_usecase"]],
                [
                    [S["chevron"], S["chevron_role"], S["chevron_use"]],
                    [S["menu"], S["menu_role"], S["menu_use"]],
                    [S["tap_take"], S["tap_take_role"], S["tap_take_use"]],
                    [S["long_press"], S["long_press_role"], S["long_press_use"]],
                    [S["import_"], S["import_role"], S["import_use"]],
                    [S["clear_slaves"], S["clear_slaves_role"], S["clear_slaves_use"]],
                ],
            )
            + callout(S["s8_note"]),
        ),
        section(
            "s9",
            S["s9_t"],
            f"<p>{S['s9_intro']}</p>"
            + f"<h3>{S['s9_mosaic']}</h3>"
            + img("07_mosaic.png", S.get("alt_mosaic", "Mosaic"))
            + f"<p>{S['s9_mosaic_p']}</p>"
            + table(
                [S["h_tool"], S["h_role"]],
                [
                    [f"<strong>{S['display_setup']}</strong>", S["ds_role"]],
                    [f"<strong>Sync</strong>", S["sync_role"]],
                    [f"<strong>{S['filter']}</strong>", S["filter_role"]],
                    [f"<strong>{S['per_guide']}</strong> <em>(Basic+)</em>", S["per_guide_role"]],
                    [f"<strong>{S['options_export']}</strong>", S["options_export_role"]],
                ],
            )
            + f"<p>{S['mosaic_audio']}</p>"
            + f"<h3>{S['s9_session']}</h3>"
            + img("08_session.png", S.get("alt_session", "Session"))
            + f"<p>{S['s9_session_p']}</p>"
            + f"<p>{S['s9_session_note']}</p>"
            + f"<h3>{S['s9_cuts']}</h3>"
            + img("09_cuts.png", S.get("alt_cuts", "Cuts"))
            + f"<p>{S['s9_cuts_p']}</p>"
            + table(
                [S["h_need"], S["h_tab"]],
                [
                    [S["need_mosaic"], "<strong>Mosaic</strong>"],
                    [S["need_session"], "<strong>Session</strong>"],
                    [S["need_cuts"], "<strong>Cuts</strong>"],
                ],
            ),
        ),
        section(
            "s10",
            S["s10_t"],
            table(
                [S["h_setting"], S["h_role"]],
                [
                    [f"<strong>Stack</strong>", S["stack_role"]],
                    [f"<strong>{S['orientation']}</strong>", S["orientation_role"]],
                    [f"<strong>{S['frame']}</strong>", S["frame_role"]],
                    [f"<strong>{S['mask']}</strong>", S["mask_role"]],
                    [S["zoom_tools"], S["zoom_tools_role"]],
                ],
            )
            + table(
                [S["h_export_opt"], S["h_role"]],
                [
                    [S["res_opts"], S["res_opts_role"]],
                    [S["compression"], S["compression_role"]],
                    [S["skip_gaps"], S["skip_gaps_role"]],
                ],
            )
            + f"<p>{S['s10_note']}</p>",
        ),
        section(
            "s11",
            S["s11_t"],
            img("06_license.png", S["alt_license"])
            + table(
                ["", "Free", "Basic"],
                [
                    [S["row_cams"], "2", "4"],
                    [S["row_mosaic"], S["yes"], S["yes"]],
                    ["Cuts", S["no"], S["yes"]],
                    [S["row_export"], S["free_export"], S["basic_export"]],
                    [S["row_guides"], S["free_guides"], S["yes"]],
                    [S["row_night"], S["no"], S["yes"]],
                ],
            )
            + f"<p>{S['s11_p']}</p>",
        ),
        section(
            "s12",
            S["s12_t"],
            f"<h3>{S['wf_classic_t']}</h3><ol>"
            + "".join(f"<li>{x}</li>" for x in S["wf_classic"])
            + f"</ol><h3>{S['wf_instant_t']}</h3><ol>"
            + "".join(f"<li>{x}</li>" for x in S["wf_instant"])
            + f"</ol><h3>{S['wf_single_t']}</h3><p>{S['wf_single_p']}</p>",
        ),
    ]
    return {
        "tag": S["tag"],
        "h1": S["h1"],
        "lead": S["lead"],
        "videos_h2": S["videos_h2"],
        "toc_h2": S["toc_h2"],
        "videos": videos,
        "sections": sections,
    }


# Load EN/FR full packs (rich HTML) + extras built from string maps
base = json.loads(EN_FR.read_text(encoding="utf-8"))
extra_maps = json.loads(EXTRA.read_text(encoding="utf-8"))

T: dict[str, dict] = {"en": base["en"], "fr": base["fr"]}
for code, strings in extra_maps.items():
    T[code] = build_from_strings(strings)

missing = [c for c in LOCALES if c not in T]
if missing:
    raise SystemExit(f"Missing guide locales: {missing}")

js = f"""/* Auto-generated by _gen_guide_i18n.py — do not edit by hand. */
window.VW_GUIDE_I18N = {json.dumps(T, ensure_ascii=False, indent=2)};
"""
OUT.write_text(js, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), locales={sorted(T)}")
