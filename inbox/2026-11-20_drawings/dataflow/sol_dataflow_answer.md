---
kind: "model-round"
round: "2026-11-20-dataflow"
backend: "cursor"
model: "gpt-5.6-sol-max"
model_used: "gpt-5.6-sol-max"
label: "GPT 5.6 Sol, max (Cursor)"
status: "ok"
started: "2026-11-20T11:17:51+01:00"
finished: "2026-11-20T11:22:54+01:00"
seconds: 303.2
dry_run: false
input_sha256: "92a96eb8dbc8effbb7db9f64eb3bb14a7b6d0734356c42050e0eb6711737ce67"
input_bytes: 13633
workdir: "~\\AppData\\Local\\Temp\\model-round-work\\round_20261120-111750\\work_cursor_gtf4byte"
command: ["~\\AppData\\Local\\cursor-agent\\agent.CMD", "-p", "--output-format", "text", "--mode", "ask", "--sandbox", "disabled", "--trust", "--workspace", "~\\AppData\\Local\\Temp\\model-round-work\\round_20261120-111750\\work_cursor_gtf4byte", "--model", "gpt-5.6-sol-max", "The only file in this workspace is input.md. Read it and do exactly what it asks. Do not read or write anything else, do not run commands. Reply in Markdown."]
sent:
  - {"path": "brief", "bytes": 13066}
not_sent:
  []
---
# Source convention

Every factual statement and numeric constant below comes from `input.md`. “Calc” means arithmetic derived from `input.md`. No figures from memory were added.

## Level 0 — Whole system

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 980" role="img" aria-labelledby="l0-title">
  <title id="l0-title">Level 0 complete wire-rope monitoring system</title>
  <defs>
    <marker id="l0-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}
    .small{font-size:14px}.box{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}
    .store{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .note{fill:#f3f4f6;stroke:#68737d;stroke-width:1.5}
    .alt{fill:#fff3cd;stroke:#8a6d1d;stroke-width:1.5}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l0-arrow)}
    .grid{stroke:#aab3ba;stroke-width:1}
  </style>

  <text x="30" y="34" class="title">Level 0 — whole SWS data flow</text>
  <text x="1170" y="34" text-anchor="end" class="small">Every label and number: input.md; “calc” means derived arithmetic</text>

  <rect x="20" y="90" width="200" height="155" rx="10" class="box"/>
  <text x="120" y="120" text-anchor="middle" class="head">Rope and SWS</text>
  <text x="120" y="148" text-anchor="middle">SWS = one head</text>
  <text x="120" y="174" text-anchor="middle">2 halves per SWS</text>
  <text x="120" y="200" text-anchor="middle">16 elements and</text>
  <text x="120" y="222" text-anchor="middle">16 channels per half</text>

  <rect x="340" y="90" width="180" height="155" rx="10" class="box"/>
  <text x="430" y="120" text-anchor="middle" class="head">Root box</text>
  <text x="430" y="150" text-anchor="middle">Check and stamp</text>
  <text x="430" y="176" text-anchor="middle">Buffer and forward</text>
  <text x="430" y="202" text-anchor="middle">No signal processing</text>
  <text x="430" y="226" text-anchor="middle" class="small">2 or 4 half ports</text>

  <rect x="630" y="90" width="150" height="155" rx="10" class="box"/>
  <text x="705" y="120" text-anchor="middle" class="head">Network</text>
  <text x="705" y="152" text-anchor="middle">Ethernet</text>
  <text x="705" y="180" text-anchor="middle">MQTT QoS 1</text>
  <text x="705" y="208" text-anchor="middle">Topic per half</text>

  <rect x="880" y="90" width="130" height="155" rx="10" class="box"/>
  <text x="945" y="120" text-anchor="middle" class="head">Logger</text>
  <text x="945" y="152" text-anchor="middle">Store raw</text>
  <text x="945" y="180" text-anchor="middle">Order and time</text>
  <text x="945" y="208" text-anchor="middle">Detect runs</text>

  <rect x="1080" y="90" width="100" height="155" rx="10" class="store"/>
  <text x="1130" y="120" text-anchor="middle" class="head">Storage</text>
  <text x="1130" y="154" text-anchor="middle">Raw</text>
  <text x="1130" y="180" text-anchor="middle">Indexes</text>
  <text x="1130" y="206" text-anchor="middle">Results</text>

  <line x1="220" y1="165" x2="340" y2="165" class="arrow"/>
  <text x="280" y="104" text-anchor="middle" class="small">4,000 values/s/half</text>
  <text x="280" y="124" text-anchor="middle" class="small">12,290 frame B/s</text>
  <text x="280" y="144" text-anchor="middle" class="small">≈12,350 serial B/s (calc)</text>

  <line x1="520" y1="165" x2="630" y2="165" class="arrow"/>
  <text x="575" y="104" text-anchor="middle" class="small">4,000 values/s/half</text>
  <text x="575" y="124" text-anchor="middle" class="small">12,380 raw B/s (calc)</text>
  <text x="575" y="144" text-anchor="middle" class="small">plus unspecified overhead</text>

  <line x1="780" y1="165" x2="880" y2="165" class="arrow"/>
  <text x="830" y="104" text-anchor="middle" class="small">4,000 values/s/half</text>
  <text x="830" y="124" text-anchor="middle" class="small">12,380 raw B/s (calc)</text>
  <text x="830" y="144" text-anchor="middle" class="small">health size unspecified</text>

  <line x1="1010" y1="165" x2="1080" y2="165" class="arrow"/>
  <text x="1045" y="104" text-anchor="middle" class="small">4,000 values/s/half</text>
  <text x="1045" y="124" text-anchor="middle" class="small">12,420 record B/s</text>
  <text x="1045" y="144" text-anchor="middle" class="small">(calc)</text>

  <line x1="340" y1="265" x2="220" y2="265" class="arrow"/>
  <text x="280" y="288" text-anchor="middle" class="small">1 sync edge/s; 0 B/s on the edge pair</text>

  <text x="30" y="330" class="head">250 values/s/channel and 100 ms frame case</text>
  <rect x="20" y="350" width="1160" height="340" class="note"/>
  <line x1="20" y1="390" x2="1180" y2="390" class="grid"/>
  <line x1="20" y1="450" x2="1180" y2="450" class="grid"/>
  <line x1="20" y1="510" x2="1180" y2="510" class="grid"/>
  <line x1="20" y1="570" x2="1180" y2="570" class="grid"/>
  <line x1="20" y1="630" x2="1180" y2="630" class="grid"/>
  <line x1="250" y1="350" x2="250" y2="690" class="grid"/>
  <line x1="330" y1="350" x2="330" y2="690" class="grid"/>
  <line x1="545" y1="350" x2="545" y2="690" class="grid"/>
  <line x1="755" y1="350" x2="755" y2="690" class="grid"/>
  <line x1="970" y1="350" x2="970" y2="690" class="grid"/>

  <text x="30" y="377" class="small">Unit</text>
  <text x="265" y="377" class="small">Halves</text>
  <text x="345" y="377" class="small">Values/s</text>
  <text x="560" y="377" class="small">Encoded serial B/s</text>
  <text x="770" y="377" class="small">Raw MQTT B/s</text>
  <text x="985" y="377" class="small">Stored-record B/s</text>

  <text x="30" y="425">One half</text><text x="275" y="425">1</text>
  <text x="345" y="416" class="small">16 × 250</text><text x="345" y="437" class="small">= 4,000</text>
  <text x="560" y="416" class="small">10 × (1,229 + ≈5 + 1)</text><text x="560" y="437" class="small">≈ 12,350</text>
  <text x="770" y="416" class="small">10 × (1,229 + 9)</text><text x="770" y="437" class="small">= 12,380</text>
  <text x="985" y="416" class="small">10 × (4 + 1,229 + 9)</text><text x="985" y="437" class="small">= 12,420</text>

  <text x="30" y="485">One SWS / first winch</text><text x="275" y="485">2</text>
  <text x="345" y="485">2 × 4,000 = 8,000</text><text x="560" y="485">2 × 12,350 = 24,700</text>
  <text x="770" y="485">2 × 12,380 = 24,760</text><text x="985" y="485">2 × 12,420 = 24,840</text>

  <text x="30" y="545">Large winch / root box</text><text x="275" y="545">4</text>
  <text x="345" y="545">4 × 4,000 = 16,000</text><text x="560" y="545">4 × 12,350 = 49,400</text>
  <text x="770" y="545">4 × 12,380 = 49,520</text><text x="985" y="545">4 × 12,420 = 49,680</text>

  <text x="30" y="605">First installation</text><text x="275" y="605">12</text>
  <text x="345" y="605">12 × 4,000 = 48,000</text><text x="560" y="605">12 × 12,350 = 148,200</text>
  <text x="770" y="605">12 × 12,380 = 148,560</text><text x="985" y="605">12 × 12,420 = 149,040</text>

  <text x="30" y="665">Large installation</text><text x="275" y="665">204</text>
  <text x="345" y="665">204 × 4,000 = 816,000</text><text x="560" y="665">204 × 12,350 = 2,519,400</text>
  <text x="770" y="665">204 × 12,380 = 2,525,520</text><text x="985" y="665">204 × 12,420 = 2,533,680</text>

  <rect x="20" y="715" width="1160" height="115" rx="8" class="alt"/>
  <text x="35" y="742" class="head">Alternatives shown without choosing</text>
  <text x="35" y="768">Line rates 80 | 100 | 125 | 250 values/s/channel give 1,280 | 1,600 | 2,000 | 4,000 values/s/half (calc).</text>
  <text x="35" y="794">Full B/s for 80, 100 and 125 cannot be derived because their frame size or cadence is not specified.</text>
  <text x="35" y="818">Serial rates: 460.8 kbit/s | alternative 1 Mbit/s. Rope speeds: 3.2 m/min normal | 5 m/min fast.</text>

  <text x="30" y="858" class="small">Buffers stated: 2-half box ≈89 MB/h; 4-half box ≈178 MB/h; first installation 6 × 89 = 534 MB/h;</text>
  <text x="30" y="880" class="small">large installation 51 × 178 = 9,078 MB/h. Raw network totals exclude MQTT, topic, TCP and Ethernet overhead.</text>
  <text x="30" y="912" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="934" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="956" class="small">Source: input.md. The first installation has one SWS and one root box per winch.</text>
</svg>
```

The rope passes through each head, and every half sends its unchanged raw frame through a root box to the logger.  
The table scales the 250 values/s/channel and 100 ms frame case from one half to both installations.  
Source: `input.md`; “calc” is arithmetic derived from it.

## Level 1 — One winch and the two wiring variants

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 880" role="img" aria-labelledby="l1-title">
  <title id="l1-title">Level 1 one-winch wiring variants</title>
  <defs>
    <marker id="l1-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .panel{fill:#f3f4f6;stroke:#68737d;stroke-width:2}.box{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}
    .alt{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}.root{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2;fill:none;marker-end:url(#l1-arrow)}
    .bus{stroke:#8a6d1d;stroke-width:5;fill:none}
  </style>

  <text x="30" y="35" class="title">Level 1 — one large-installation winch</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md; arithmetic marked “calc”</text>

  <rect x="20" y="65" width="560" height="610" rx="10" class="panel"/>
  <text x="300" y="98" text-anchor="middle" class="head">Variant A — one point-to-point RS-422 cable per half</text>

  <rect x="45" y="125" width="270" height="190" rx="8" class="box"/>
  <text x="60" y="150" class="head">SWS/head 1 — 2 halves</text>
  <rect x="65" y="170" width="225" height="55" rx="6" class="box"/>
  <rect x="65" y="240" width="225" height="55" rx="6" class="box"/>
  <text x="78" y="193">Half 1A: 16 elements, 16 channels</text>
  <text x="78" y="263">Half 1B: 16 elements, 16 channels</text>

  <rect x="45" y="340" width="270" height="190" rx="8" class="box"/>
  <text x="60" y="365" class="head">SWS/head 2 — 2 halves</text>
  <rect x="65" y="385" width="225" height="55" rx="6" class="box"/>
  <rect x="65" y="455" width="225" height="55" rx="6" class="box"/>
  <text x="78" y="408">Half 2A: 16 elements, 16 channels</text>
  <text x="78" y="478">Half 2B: 16 elements, 16 channels</text>

  <rect x="395" y="235" width="155" height="185" rx="8" class="root"/>
  <text x="472" y="266" text-anchor="middle" class="head">One root box</text>
  <text x="472" y="296" text-anchor="middle">4 half ports</text>
  <text x="472" y="324" text-anchor="middle">1 Hz edge to all</text>
  <text x="472" y="352" text-anchor="middle">24 V supply</text>
  <text x="472" y="380" text-anchor="middle">5–100 m cables</text>

  <line x1="290" y1="197" x2="395" y2="270" class="arrow"/>
  <line x1="290" y1="267" x2="395" y2="305" class="arrow"/>
  <line x1="290" y1="412" x2="395" y2="350" class="arrow"/>
  <line x1="290" y1="482" x2="395" y2="385" class="arrow"/>
  <text x="300" y="565" text-anchor="middle" class="small">Each line: 4,000 values/s and ≈12,350 encoded B/s (250 case, calc)</text>
  <text x="300" y="588" text-anchor="middle" class="small">Each cable: data both ways, separate 1 Hz pair and 24 V; reverse data B/s unspecified</text>
  <text x="300" y="613" text-anchor="middle">Four lines total: 16,000 values/s and ≈49,400 B/s (calc)</text>
  <text x="300" y="638" text-anchor="middle">460.8 kbit/s | alternative 1 Mbit/s</text>

  <rect x="620" y="65" width="560" height="610" rx="10" class="alt"/>
  <text x="900" y="98" text-anchor="middle" class="head">Variant B — shared four-wire RS-485, polled</text>

  <rect x="645" y="125" width="260" height="190" rx="8" class="box"/>
  <text x="660" y="150" class="head">SWS/head 1 — 2 halves</text>
  <rect x="665" y="170" width="220" height="55" rx="6" class="box"/>
  <rect x="665" y="240" width="220" height="55" rx="6" class="box"/>
  <text x="678" y="193">Half 1A: 16 elements, 16 channels</text>
  <text x="678" y="263">Half 1B: 16 elements, 16 channels</text>

  <rect x="645" y="340" width="260" height="190" rx="8" class="box"/>
  <text x="660" y="365" class="head">SWS/head 2 — 2 halves</text>
  <rect x="665" y="385" width="220" height="55" rx="6" class="box"/>
  <rect x="665" y="455" width="220" height="55" rx="6" class="box"/>
  <text x="678" y="408">Half 2A: 16 elements, 16 channels</text>
  <text x="678" y="478">Half 2B: 16 elements, 16 channels</text>

  <line x1="930" y1="165" x2="930" y2="500" class="bus"/>
  <line x1="885" y1="197" x2="930" y2="197" class="bus"/>
  <line x1="885" y1="267" x2="930" y2="267" class="bus"/>
  <line x1="885" y1="412" x2="930" y2="412" class="bus"/>
  <line x1="885" y1="482" x2="930" y2="482" class="bus"/>

  <rect x="1000" y="235" width="150" height="185" rx="8" class="root"/>
  <text x="1075" y="266" text-anchor="middle" class="head">One root box</text>
  <text x="1075" y="298" text-anchor="middle">Polls 4 halves</text>
  <text x="1075" y="330" text-anchor="middle">Shared line</text>
  <text x="1075" y="362" text-anchor="middle">Not built</text>
  <line x1="930" y1="328" x2="1000" y2="328" class="arrow"/>

  <text x="900" y="565" text-anchor="middle">Generated payload: 16,000 values/s</text>
  <text x="900" y="590" text-anchor="middle">≈49,400 encoded B/s if frames are unchanged (calc)</text>
  <text x="900" y="615" text-anchor="middle">Polling bytes and actual shared-bus B/s are unspecified</text>
  <text x="900" y="640" text-anchor="middle">460.8 kbit/s | alternative 1 Mbit/s</text>

  <rect x="20" y="700" width="1160" height="65" rx="8" class="panel"/>
  <text x="35" y="728">First installation per winch: 1 SWS/head = 2 halves, 1 root box, so only two half connections are used.</text>
  <text x="35" y="752">Both variants remain alternatives; the shared RS-485 variant is not built in the code.</text>

  <text x="30" y="797" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="819" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="841" class="small">Source: input.md.</text>
</svg>
```

The left side gives every half its own RS-422 cable, while the right side puts four halves on one polled RS-485 line.  
A first-installation winch has only one SWS and two halves; a large-installation winch has two SWS and four halves.  
Source: `input.md`; the shared-line payload estimate is arithmetic from it.

## Level 2A — Inside one half

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" role="img" aria-labelledby="l2h-title">
  <title id="l2h-title">Level 2 inside one half</title>
  <defs>
    <marker id="l2h-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .box{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.alt{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .note{fill:#f3f4f6;stroke:#68737d;stroke-width:1.5}.out{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l2h-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 2A — inside one half</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="245" width="180" height="190" rx="8" class="box"/>
  <text x="110" y="277" text-anchor="middle" class="head">16 sensing elements</text>
  <text x="110" y="310" text-anchor="middle">8 radial</text>
  <text x="110" y="338" text-anchor="middle">8 axial</text>
  <text x="110" y="370" text-anchor="middle">16 signed</text>
  <text x="110" y="396" text-anchor="middle">24-bit values</text>

  <rect x="235" y="200" width="220" height="285" rx="8" class="box"/>
  <text x="345" y="232" text-anchor="middle" class="head">Two delta-sigma converters</text>
  <text x="345" y="266" text-anchor="middle">Converter 1: channels 0–7</text>
  <text x="345" y="292" text-anchor="middle">radial in the frame</text>
  <text x="345" y="326" text-anchor="middle">Converter 2: channels 8–15</text>
  <text x="345" y="352" text-anchor="middle">axial in the frame</text>
  <text x="345" y="388" text-anchor="middle">1,000–4,000 results/s/channel</text>
  <text x="345" y="416" text-anchor="middle">4,000 starting code value</text>
  <text x="345" y="448" text-anchor="middle">One 16-value result set/call</text>

  <rect x="235" y="80" width="220" height="85" rx="8" class="note"/>
  <text x="345" y="110" text-anchor="middle" class="head">One crystal</text>
  <text x="345" y="137" text-anchor="middle">Clocks both converters</text>
  <line x1="345" y1="165" x2="345" y2="200" class="arrow"/>
  <text x="475" y="118" class="small">One joint synchronising pulse at start-up;</text>
  <text x="475" y="140" class="small">no converter reset during a run</text>

  <rect x="500" y="125" width="260" height="210" rx="8" class="box"/>
  <text x="630" y="157" text-anchor="middle" class="head">Three-stage alternative</text>
  <text x="630" y="185" text-anchor="middle">Starting code value</text>
  <text x="630" y="215" text-anchor="middle">Three integrators/channel</text>
  <text x="630" y="241" text-anchor="middle">Three combs every n results</text>
  <text x="630" y="269" text-anchor="middle">(sum + n³/2) / n³</text>
  <text x="630" y="297" text-anchor="middle">Then (−y[k] + 10y[k−1]</text>
  <text x="630" y="319" text-anchor="middle">− y[k−2] + 4) &gt;&gt; 3</text>

  <rect x="500" y="375" width="260" height="140" rx="8" class="alt"/>
  <text x="630" y="407" text-anchor="middle" class="head">Block alternative</text>
  <text x="630" y="441" text-anchor="middle">One block average</text>
  <text x="630" y="471" text-anchor="middle">(sum of n results + n/2) / n</text>
  <text x="630" y="497" text-anchor="middle">Integer arithmetic</text>

  <rect x="795" y="225" width="175" height="220" rx="8" class="box"/>
  <text x="882" y="257" text-anchor="middle" class="head">Line samples</text>
  <text x="882" y="288" text-anchor="middle">250/channel/s</text>
  <text x="882" y="314" text-anchor="middle">Alternatives:</text>
  <text x="882" y="340" text-anchor="middle">80 | 100 | 125</text>
  <text x="882" y="372" text-anchor="middle">Clamp each value</text>
  <text x="882" y="398" text-anchor="middle">to −2²³ … 2²³−1</text>
  <text x="882" y="424" text-anchor="middle">No clamp health bit</text>

  <rect x="1000" y="175" width="180" height="330" rx="8" class="out"/>
  <text x="1090" y="207" text-anchor="middle" class="head">Frame and line</text>
  <text x="1090" y="240" text-anchor="middle">Every 100 ms</text>
  <text x="1090" y="268" text-anchor="middle">25 × 16 × 3</text>
  <text x="1090" y="294" text-anchor="middle">= 1,200 value bytes</text>
  <text x="1090" y="324" text-anchor="middle">25-byte header</text>
  <text x="1090" y="350" text-anchor="middle">4-byte CRC-32C</text>
  <text x="1090" y="378" text-anchor="middle">= 1,229 bytes</text>
  <text x="1090" y="410" text-anchor="middle">COBS + 00h</text>
  <text x="1090" y="436" text-anchor="middle">8N1, 10 bits/byte</text>
  <text x="1090" y="464" text-anchor="middle">RS-422 line driver</text>
  <text x="1090" y="488" text-anchor="middle" class="small">460.8 kbit/s | 1 Mbit/s</text>

  <line x1="200" y1="340" x2="235" y2="340" class="arrow"/>
  <line x1="455" y1="300" x2="500" y2="230" class="arrow"/>
  <line x1="455" y1="380" x2="500" y2="445" class="arrow"/>
  <line x1="760" y1="230" x2="795" y2="300" class="arrow"/>
  <line x1="760" y1="445" x2="795" y2="380" class="arrow"/>
  <line x1="970" y1="335" x2="1000" y2="335" class="arrow"/>

  <rect x="20" y="565" width="1160" height="180" rx="8" class="note"/>
  <text x="35" y="597" class="head">Microcontroller state and side inputs</text>
  <text x="35" y="627">Caller-owned state: configuration, boot and health flags, edge capture, u32 line index, u64 result count, filter state and two frame buffers.</text>
  <text x="35" y="657">The digital temperature part supplies two i16 frame temperatures when a new reading exists; each unit is 0.01 °C.</text>
  <text x="35" y="687">A 1 Hz interrupt records the pending converter-result position; every frame carries the latched line index and u16/65,536 fraction.</text>
  <text x="35" y="717">No high-pass, offset removal or scaling occurs. A constant input passes unchanged.</text>

  <text x="30" y="785" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="807" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="829" class="small">Source: input.md. Both filter choices and all line-rate choices remain alternatives.</text>
</svg>
```

One half converts 16 magnetic-field values, applies one of two integer filters and packs line samples into frames.  
A shared crystal and start-up pulse align its two converters, while the 1 Hz edge supplies a long-term timing reference.  
Source: `input.md`; no filter or rate alternative has been selected here.

## Level 2B — Inside the root box

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 870" role="img" aria-labelledby="l2r-title">
  <title id="l2r-title">Level 2 inside the root box</title>
  <defs>
    <marker id="l2r-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .box{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.alt{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .note{fill:#f3f4f6;stroke:#68737d;stroke-width:1.5}.out{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l2r-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 2B — inside one root box</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="180" width="195" height="265" rx="8" class="box"/>
  <text x="117" y="212" text-anchor="middle" class="head">Receive per port</text>
  <text x="117" y="246" text-anchor="middle">Split at 00h</text>
  <text x="117" y="274" text-anchor="middle">COBS-decode</text>
  <text x="117" y="306" text-anchor="middle">2 ports: first box</text>
  <text x="117" y="334" text-anchor="middle">4 ports: large box</text>
  <text x="117" y="368" text-anchor="middle">Count bytes in</text>
  <text x="117" y="398" text-anchor="middle">10 frames/s/half</text>

  <rect x="245" y="180" width="195" height="265" rx="8" class="box"/>
  <text x="342" y="212" text-anchor="middle" class="head">Check</text>
  <text x="342" y="246" text-anchor="middle">Length = 1,229</text>
  <text x="342" y="274" text-anchor="middle">CRC-32C valid</text>
  <text x="342" y="302" text-anchor="middle">Type = 0x11</text>
  <text x="342" y="330" text-anchor="middle">Half id matches port</text>
  <text x="342" y="364" text-anchor="middle">Bad or wrong:</text>
  <text x="342" y="392" text-anchor="middle">count and drop</text>

  <rect x="470" y="150" width="225" height="325" rx="8" class="box"/>
  <text x="582" y="182" text-anchor="middle" class="head">Time and continuity</text>
  <text x="582" y="216" text-anchor="middle">Compare boot and first index</text>
  <text x="582" y="244" text-anchor="middle">Lower: duplicate, drop</text>
  <text x="582" y="272" text-anchor="middle">Higher: count gap</text>
  <text x="582" y="300" text-anchor="middle">New boot: restart</text>
  <text x="582" y="328" text-anchor="middle">Estimate silent frames</text>
  <text x="582" y="360" text-anchor="middle">Append u64 receive time</text>
  <text x="582" y="388" text-anchor="middle">and u8 quality = 9 bytes</text>
  <text x="582" y="420" text-anchor="middle">Carry edge metadata;</text>
  <text x="582" y="446" text-anchor="middle">do not align samples here</text>

  <rect x="725" y="150" width="210" height="325" rx="8" class="alt"/>
  <text x="830" y="182" text-anchor="middle" class="head">Disk buffer</text>
  <text x="830" y="216" text-anchor="middle">Append-only segments</text>
  <text x="830" y="244" text-anchor="middle">Length-prefixed records</text>
  <text x="830" y="278" text-anchor="middle">24 h starting value</text>
  <text x="830" y="306" text-anchor="middle">Alternatives: 1 | 72 | 720 h</text>
  <text x="830" y="338" text-anchor="middle">Cap: 4,096 MB</text>
  <text x="830" y="370" text-anchor="middle">Remove oldest segment</text>
  <text x="830" y="398" text-anchor="middle">and count records lost</text>
  <text x="830" y="430" text-anchor="middle">Replay oldest first</text>
  <text x="830" y="456" text-anchor="middle">Quality bit 4 when held</text>

  <rect x="965" y="150" width="215" height="325" rx="8" class="out"/>
  <text x="1072" y="182" text-anchor="middle" class="head">Publish, MQTT QoS 1</text>
  <text x="1072" y="216" text-anchor="middle">One raw message</text>
  <text x="1072" y="244" text-anchor="middle">per half per frame</text>
  <text x="1072" y="272" text-anchor="middle">1,229 + 9 = 1,238 B</text>
  <text x="1072" y="306" text-anchor="middle">Raw topic per half</text>
  <text x="1072" y="334" text-anchor="middle">Health once/s/half</text>
  <text x="1072" y="362" text-anchor="middle">Status retained at start</text>
  <text x="1072" y="396" text-anchor="middle">Alternative:</text>
  <text x="1072" y="424" text-anchor="middle">one message/box/s</text>
  <text x="1072" y="452" text-anchor="middle">not built</text>

  <line x1="215" y1="312" x2="245" y2="312" class="arrow"/>
  <line x1="440" y1="312" x2="470" y2="312" class="arrow"/>
  <line x1="695" y1="312" x2="725" y2="312" class="arrow"/>
  <line x1="935" y1="312" x2="965" y2="312" class="arrow"/>

  <rect x="20" y="510" width="1160" height="190" rx="8" class="note"/>
  <text x="35" y="542" class="head">Timing, topics and quality</text>
  <text x="35" y="574">The root box sends one 1 Hz edge to all halves together; real edge output and clock discipline are not built.</text>
  <text x="35" y="604">Quality: bit 1 = gap before, bit 2 = after restart, bit 4 = held in buffer.</text>
  <text x="35" y="634">Raw: sws/&lt;installation&gt;/&lt;winch&gt;/&lt;head&gt;/&lt;half&gt;/raw; health uses …/health.</text>
  <text x="35" y="664">Status: sws/&lt;installation&gt;/&lt;box&gt;/status. The root box performs no scaling, filtering or detection.</text>

  <text x="30" y="744" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="766" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="788" class="small">Source: input.md. “Time and continuity” carries alignment metadata; sample-time alignment occurs in the logger.</text>
</svg>
```

The root box validates each serial frame, detects continuity problems, adds nine bytes and forwards or buffers it.  
It distributes the 1 Hz edge but does no signal filtering, scaling, detection or sample-time alignment.  
Source: `input.md`; the one-message-per-box design remains an unbuilt alternative.

## Level 2C — Inside the logger

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" role="img" aria-labelledby="l2l-title">
  <title id="l2l-title">Level 2 inside the logger</title>
  <defs>
    <marker id="l2l-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .box{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.store{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .note{fill:#f3f4f6;stroke:#68737d;stroke-width:1.5}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l2l-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 2C — inside the logger</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="150" width="175" height="250" rx="8" class="box"/>
  <text x="107" y="182" text-anchor="middle" class="head">Receive</text>
  <text x="107" y="216" text-anchor="middle">Subscribe to raw</text>
  <text x="107" y="244" text-anchor="middle">health and status</text>
  <text x="107" y="278" text-anchor="middle">Raw payload:</text>
  <text x="107" y="306" text-anchor="middle">1,238 bytes/frame</text>
  <text x="107" y="340" text-anchor="middle">10 frames/s/half</text>
  <text x="107" y="372" text-anchor="middle">MQTT QoS 1</text>

  <rect x="225" y="115" width="220" height="320" rx="8" class="store"/>
  <text x="335" y="147" text-anchor="middle" class="head">Store raw and index</text>
  <text x="335" y="181" text-anchor="middle">u32 length + message</text>
  <text x="335" y="209" text-anchor="middle">= 1,242 B/record</text>
  <text x="335" y="243" text-anchor="middle">Keep every raw message</text>
  <text x="335" y="275" text-anchor="middle">Index: offset, length,</text>
  <text x="335" y="301" text-anchor="middle">winch, head, half, id,</text>
  <text x="335" y="327" text-anchor="middle">boot, index, samples,</text>
  <text x="335" y="353" text-anchor="middle">receive time, quality,</text>
  <text x="335" y="379" text-anchor="middle">first-sample time</text>
  <text x="335" y="411" text-anchor="middle">≈44.6 MB/half/run hour</text>

  <rect x="475" y="115" width="215" height="320" rx="8" class="box"/>
  <text x="582" y="147" text-anchor="middle" class="head">Order and time</text>
  <text x="582" y="181" text-anchor="middle">Order by boot, first index</text>
  <text x="582" y="209" text-anchor="middle">Hold up to 50 frames</text>
  <text x="582" y="237" text-anchor="middle">Count unresolved gaps</text>
  <text x="582" y="269" text-anchor="middle">New boot = restart</text>
  <text x="582" y="303" text-anchor="middle">Use latch + fraction</text>
  <text x="582" y="331" text-anchor="middle">and line rate</text>
  <text x="582" y="359" text-anchor="middle">Add filter delay</text>
  <text x="582" y="391" text-anchor="middle">Receive time chooses</text>
  <text x="582" y="417" text-anchor="middle">the whole edge second</text>

  <rect x="720" y="115" width="215" height="320" rx="8" class="box"/>
  <text x="827" y="147" text-anchor="middle" class="head">Detect and cut runs</text>
  <text x="827" y="181" text-anchor="middle">One-second windows</text>
  <text x="827" y="209" text-anchor="middle">Mains-period mean</text>
  <text x="827" y="237" text-anchor="middle">Remove mean and slope</text>
  <text x="827" y="265" text-anchor="middle">Median channel RMS</text>
  <text x="827" y="293" text-anchor="middle">in strand-ripple band</text>
  <text x="827" y="325" text-anchor="middle">Above 2 s = moving</text>
  <text x="827" y="353" text-anchor="middle">Below 10 s = stopped</text>
  <text x="827" y="381" text-anchor="middle">Keep 30 s before/after</text>
  <text x="827" y="409" text-anchor="middle">Stop &lt;75 s: same run</text>

  <rect x="965" y="115" width="215" height="320" rx="8" class="box"/>
  <text x="1072" y="147" text-anchor="middle" class="head">Position and results</text>
  <text x="1072" y="181" text-anchor="middle">Count strand ripple</text>
  <text x="1072" y="209" text-anchor="middle">Use ramps and fixed length</text>
  <text x="1072" y="237" text-anchor="middle">Register to first run</text>
  <text x="1072" y="265" text-anchor="middle">within half a pitch</text>
  <text x="1072" y="293" text-anchor="middle">312 mm level trace</text>
  <text x="1072" y="321" text-anchor="middle">Drift and temperature</text>
  <text x="1072" y="349" text-anchor="middle">correction</text>
  <text x="1072" y="377" text-anchor="middle">Radial peaks above</text>
  <text x="1072" y="405" text-anchor="middle">a threshold</text>

  <line x1="195" y1="275" x2="225" y2="275" class="arrow"/>
  <line x1="445" y1="275" x2="475" y2="275" class="arrow"/>
  <line x1="690" y1="275" x2="720" y2="275" class="arrow"/>
  <line x1="935" y1="275" x2="965" y2="275" class="arrow"/>

  <rect x="225" y="490" width="955" height="200" rx="8" class="store"/>
  <text x="702" y="522" text-anchor="middle" class="head">Run files</text>
  <text x="245" y="558">For each head and run: raw frames per half, one index per half, a run description and results.</text>
  <text x="245" y="590">Raw frames remain beside every result; processed output is never the only copy.</text>
  <text x="245" y="622">Both installations have proximity switches at each end of fixed travel.</text>
  <text x="245" y="654">The first installation has no plant-control connection and derives movement and position from its own data.</text>
  <line x1="827" y1="435" x2="827" y2="490" class="arrow"/>
  <line x1="1072" y1="435" x2="1072" y2="490" class="arrow"/>

  <text x="30" y="744" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="766" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="788" class="small">Source: input.md. Live run files are not built; current files are written when a session closes.</text>
</svg>
```

The logger first keeps every received raw message, then orders, times and processes the data.  
Movement creates runs, and strand ripple supplies position, registration and the measurements written beside the raw data.  
Source: `input.md`; no processing result replaces the raw frames.

## Level 3A — Half acquisition, edge and line-sample sequence

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" role="img" aria-labelledby="l3h1-title">
  <title id="l3h1-title">Level 3 half acquisition state sequence</title>
  <defs>
    <marker id="l3h1-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .state{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.event{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .done{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l3h1-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 3A — L3-H1 HALF_ACQUIRE</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="170" width="150" height="120" rx="12" class="state"/>
  <text x="95" y="205" text-anchor="middle" class="head">WAIT_RESULT</text>
  <text x="95" y="236" text-anchor="middle">16 × i24</text>
  <text x="95" y="264" text-anchor="middle">one result set</text>

  <rect x="205" y="145" width="185" height="170" rx="12" class="state"/>
  <text x="297" y="180" text-anchor="middle" class="head">FILTER_RESULT</text>
  <text x="297" y="212" text-anchor="middle">Three-stage:</text>
  <text x="297" y="238" text-anchor="middle">3 integrators</text>
  <text x="297" y="266" text-anchor="middle">or block sum</text>
  <text x="297" y="294" text-anchor="middle">for all 16 channels</text>

  <rect x="425" y="155" width="160" height="150" rx="12" class="state"/>
  <text x="505" y="190" text-anchor="middle" class="head">DECIMATE</text>
  <text x="505" y="222" text-anchor="middle">Only every n-th</text>
  <text x="505" y="250" text-anchor="middle">converter result</text>
  <text x="505" y="278" text-anchor="middle">makes a line sample</text>

  <rect x="620" y="145" width="205" height="170" rx="12" class="state"/>
  <text x="722" y="180" text-anchor="middle" class="head">CORRECT_AND_CLAMP</text>
  <text x="722" y="214" text-anchor="middle">Three taps or</text>
  <text x="722" y="242" text-anchor="middle">block result</text>
  <text x="722" y="270" text-anchor="middle">Clamp to signed i24</text>
  <text x="722" y="298" text-anchor="middle">No scaling</text>

  <rect x="860" y="155" width="155" height="150" rx="12" class="state"/>
  <text x="937" y="190" text-anchor="middle" class="head">PACK_LINE_SAMPLE</text>
  <text x="937" y="226" text-anchor="middle">16 × 3 bytes</text>
  <text x="937" y="254" text-anchor="middle">Increment u32</text>
  <text x="937" y="282" text-anchor="middle">line index</text>

  <rect x="1050" y="155" width="130" height="150" rx="12" class="done"/>
  <text x="1115" y="190" text-anchor="middle" class="head">COMPLETE_FRAME</text>
  <text x="1115" y="226" text-anchor="middle">At 25</text>
  <text x="1115" y="254" text-anchor="middle">samples</text>
  <text x="1115" y="282" text-anchor="middle">else loop</text>

  <line x1="170" y1="230" x2="205" y2="230" class="arrow"/>
  <line x1="390" y1="230" x2="425" y2="230" class="arrow"/>
  <line x1="585" y1="230" x2="620" y2="230" class="arrow"/>
  <line x1="825" y1="230" x2="860" y2="230" class="arrow"/>
  <line x1="1015" y1="230" x2="1050" y2="230" class="arrow"/>
  <path d="M505,305 C505,370 95,370 95,290" class="arrow"/>
  <text x="305" y="355" text-anchor="middle">Not the n-th result: return to WAIT_RESULT</text>

  <rect x="170" y="450" width="225" height="135" rx="12" class="event"/>
  <text x="282" y="485" text-anchor="middle" class="head">CAPTURE_EDGE</text>
  <text x="282" y="519" text-anchor="middle">Interrupt before next result</text>
  <text x="282" y="547" text-anchor="middle">Store pending u64</text>
  <text x="282" y="575" text-anchor="middle">converter-result index</text>

  <rect x="475" y="450" width="250" height="135" rx="12" class="event"/>
  <text x="600" y="485" text-anchor="middle" class="head">APPLY_PENDING_EDGE</text>
  <text x="600" y="519" text-anchor="middle">At next completed line sample</text>
  <text x="600" y="547" text-anchor="middle">Set u32 latch and</text>
  <text x="600" y="575" text-anchor="middle">u16 fraction / 65,536</text>

  <line x1="395" y1="518" x2="475" y2="518" class="arrow"/>
  <path d="M600,450 C600,390 937,390 937,305" class="arrow"/>
  <text x="830" y="415" text-anchor="middle">Latched into the next frame that completes</text>

  <rect x="795" y="450" width="385" height="135" rx="12" class="state"/>
  <text x="987" y="485" text-anchor="middle" class="head">Line-sample outcome</text>
  <text x="987" y="519" text-anchor="middle">250 values/s/channel starting line rate</text>
  <text x="987" y="547" text-anchor="middle">Alternatives: 80 | 100 | 125</text>
  <text x="987" y="575" text-anchor="middle">4,000 values/s/half at 250 (calc)</text>

  <text x="30" y="685" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="707" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="729" class="small">Source: input.md. Exact conversion of the captured result index into latch and fraction is not specified.</text>
</svg>
```

Each converter-result call updates the chosen filter, but only every n-th result creates one line sample.  
A pending 1 Hz edge becomes a line index and fractional position carried by the next completed frame.  
Source: `input.md`; the exact edge-to-fraction conversion is not given there.

## Level 3B — Half frame, send overflow and restart

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 840" role="img" aria-labelledby="l3h2-title">
  <title id="l3h2-title">Level 3 half frame send and restart sequence</title>
  <defs>
    <marker id="l3h2-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .state{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.event{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .done{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l3h2-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 3B — L3-H2 HALF_FRAME_AND_RESTART</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="125" width="200" height="175" rx="12" class="state"/>
  <text x="120" y="160" text-anchor="middle" class="head">COMPLETE_FRAME</text>
  <text x="120" y="194" text-anchor="middle">25-byte header</text>
  <text x="120" y="222" text-anchor="middle">1,200 value bytes</text>
  <text x="120" y="250" text-anchor="middle">CRC-32C: 4 bytes</text>
  <text x="120" y="278" text-anchor="middle">Total 1,229</text>

  <rect x="260" y="125" width="180" height="175" rx="12" class="state"/>
  <text x="350" y="160" text-anchor="middle" class="head">SWAP_BUFFERS</text>
  <text x="350" y="196" text-anchor="middle">Finished frame</text>
  <text x="350" y="224" text-anchor="middle">stays intact</text>
  <text x="350" y="252" text-anchor="middle">while next frame</text>
  <text x="350" y="280" text-anchor="middle">fills</text>

  <rect x="480" y="125" width="195" height="175" rx="12" class="event"/>
  <text x="577" y="160" text-anchor="middle" class="head">SEND_AVAILABLE?</text>
  <text x="577" y="196" text-anchor="middle">Finished-buffer</text>
  <text x="577" y="224" text-anchor="middle">consumer ready?</text>
  <text x="577" y="258" text-anchor="middle">Yes or no</text>

  <rect x="735" y="85" width="200" height="145" rx="12" class="done"/>
  <text x="835" y="120" text-anchor="middle" class="head">COBS_SEND</text>
  <text x="835" y="154" text-anchor="middle">COBS encode</text>
  <text x="835" y="182" text-anchor="middle">Append 00h</text>
  <text x="835" y="210" text-anchor="middle">8N1 serial</text>

  <rect x="735" y="270" width="240" height="145" rx="12" class="event"/>
  <text x="855" y="305" text-anchor="middle" class="head">DROP_AND_LATCH_OVERFLOW</text>
  <text x="855" y="339" text-anchor="middle">Drop this frame</text>
  <text x="855" y="367" text-anchor="middle">Set health bit 1</text>
  <text x="855" y="395" text-anchor="middle">until restart</text>

  <line x1="220" y1="212" x2="260" y2="212" class="arrow"/>
  <line x1="440" y1="212" x2="480" y2="212" class="arrow"/>
  <line x1="675" y1="180" x2="735" y2="158" class="arrow"/>
  <line x1="675" y1="245" x2="735" y2="342" class="arrow"/>
  <text x="705" y="142" class="small">yes</text><text x="692" y="312" class="small">no</text>

  <rect x="20" y="480" width="160" height="115" rx="12" class="state"/>
  <text x="100" y="515" text-anchor="middle" class="head">RUNNING</text>
  <text x="100" y="549" text-anchor="middle">No converter</text>
  <text x="100" y="577" text-anchor="middle">reset in a run</text>

  <rect x="235" y="460" width="200" height="155" rx="12" class="event"/>
  <text x="335" y="495" text-anchor="middle" class="head">RESTART</text>
  <text x="335" y="529" text-anchor="middle">Increment u8 boot</text>
  <text x="335" y="557" text-anchor="middle">Reset counters, filters,</text>
  <text x="335" y="585" text-anchor="middle">edge latch and fill frame</text>

  <rect x="490" y="480" width="170" height="115" rx="12" class="event"/>
  <text x="575" y="515" text-anchor="middle" class="head">SILENT</text>
  <text x="575" y="549" text-anchor="middle">About 2 s</text>
  <text x="575" y="577" text-anchor="middle">No frames</text>

  <rect x="715" y="460" width="240" height="155" rx="12" class="done"/>
  <text x="835" y="495" text-anchor="middle" class="head">FIRST_FRAME</text>
  <text x="835" y="529" text-anchor="middle">Health bit 0 set</text>
  <text x="835" y="557" text-anchor="middle">New boot count</text>
  <text x="835" y="585" text-anchor="middle">Then normal frames</text>

  <line x1="180" y1="537" x2="235" y2="537" class="arrow"/>
  <line x1="435" y1="537" x2="490" y2="537" class="arrow"/>
  <line x1="660" y1="537" x2="715" y2="537" class="arrow"/>
  <path d="M955,537 C1040,537 1040,680 100,680 C100,680 100,620 100,595" class="arrow"/>

  <text x="30" y="735" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="757" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="779" class="small">Source: input.md.</text>
</svg>
```

A complete frame is protected by the second buffer while the next frame starts filling.  
A busy send buffer drops one frame and latches the overflow bit; a restart clears state and causes about two silent seconds.  
Source: `input.md`.

## Level 3C — Root-box validation, loss and restart sequence

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 870" role="img" aria-labelledby="l3r1-title">
  <title id="l3r1-title">Level 3 root frame validation and continuity</title>
  <defs>
    <marker id="l3r1-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .state{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.event{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .done{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l3r1-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 3C — L3-R1 ROOT_ACCEPT_FRAME</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="135" width="175" height="145" rx="12" class="state"/>
  <text x="107" y="170" text-anchor="middle" class="head">WAIT_DELIMITER</text>
  <text x="107" y="204" text-anchor="middle">Collect bytes</text>
  <text x="107" y="232" text-anchor="middle">until 00h</text>
  <text x="107" y="260" text-anchor="middle">Count bytes in</text>

  <rect x="230" y="115" width="205" height="185" rx="12" class="state"/>
  <text x="332" y="150" text-anchor="middle" class="head">DECODE_AND_CHECK</text>
  <text x="332" y="184" text-anchor="middle">COBS and length</text>
  <text x="332" y="212" text-anchor="middle">CRC-32C</text>
  <text x="332" y="240" text-anchor="middle">type 0x11</text>
  <text x="332" y="268" text-anchor="middle">half id matches port</text>

  <rect x="470" y="115" width="205" height="185" rx="12" class="state"/>
  <text x="572" y="150" text-anchor="middle" class="head">CHECK_CONTINUITY</text>
  <text x="572" y="184" text-anchor="middle">Compare boot count</text>
  <text x="572" y="212" text-anchor="middle">and expected index</text>
  <text x="572" y="240" text-anchor="middle">Normal, duplicate,</text>
  <text x="572" y="268" text-anchor="middle">gap or restart</text>

  <rect x="715" y="115" width="215" height="185" rx="12" class="done"/>
  <text x="822" y="150" text-anchor="middle" class="head">STAMP_AND_APPEND_9</text>
  <text x="822" y="184" text-anchor="middle">u64 receive µs</text>
  <text x="822" y="212" text-anchor="middle">u8 quality</text>
  <text x="822" y="240" text-anchor="middle">Frame unchanged</text>
  <text x="822" y="268" text-anchor="middle">1,238-byte payload</text>

  <rect x="970" y="135" width="210" height="145" rx="12" class="done"/>
  <text x="1075" y="170" text-anchor="middle" class="head">ROUTE_MESSAGE</text>
  <text x="1075" y="204" text-anchor="middle">Publish now or</text>
  <text x="1075" y="232" text-anchor="middle">append to buffer</text>
  <text x="1075" y="260" text-anchor="middle">MQTT QoS 1</text>

  <line x1="195" y1="207" x2="230" y2="207" class="arrow"/>
  <line x1="435" y1="207" x2="470" y2="207" class="arrow"/>
  <line x1="675" y1="207" x2="715" y2="207" class="arrow"/>
  <line x1="930" y1="207" x2="970" y2="207" class="arrow"/>

  <rect x="80" y="390" width="230" height="135" rx="12" class="event"/>
  <text x="195" y="425" text-anchor="middle" class="head">REJECT_FRAME</text>
  <text x="195" y="459" text-anchor="middle">Bad or wrong half:</text>
  <text x="195" y="487" text-anchor="middle">count and drop</text>
  <text x="195" y="515" text-anchor="middle">Return to delimiter</text>
  <path d="M332,300 C332,350 195,350 195,390" class="arrow"/>

  <rect x="350" y="390" width="210" height="135" rx="12" class="event"/>
  <text x="455" y="425" text-anchor="middle" class="head">DROP_DUPLICATE</text>
  <text x="455" y="459" text-anchor="middle">Same boot and</text>
  <text x="455" y="487" text-anchor="middle">index below expected</text>
  <text x="455" y="515" text-anchor="middle">Count and drop</text>

  <rect x="600" y="390" width="230" height="135" rx="12" class="event"/>
  <text x="715" y="425" text-anchor="middle" class="head">GAP_ACCOUNT</text>
  <text x="715" y="459" text-anchor="middle">Index above expected</text>
  <text x="715" y="487" text-anchor="middle">lost += gap/samples</text>
  <text x="715" y="515" text-anchor="middle">quality bit 1</text>

  <rect x="870" y="390" width="250" height="135" rx="12" class="event"/>
  <text x="995" y="425" text-anchor="middle" class="head">RESTART_ACCOUNT</text>
  <text x="995" y="459" text-anchor="middle">Different boot count</text>
  <text x="995" y="487" text-anchor="middle">Estimate silent frames</text>
  <text x="995" y="515" text-anchor="middle">quality bit 2</text>

  <path d="M530,300 C530,345 455,345 455,390" class="arrow"/>
  <path d="M572,300 C572,350 715,350 715,390" class="arrow"/>
  <path d="M620,300 C620,340 995,340 995,390" class="arrow"/>
  <path d="M715,390 C715,340 822,340 822,300" class="arrow"/>
  <path d="M995,390 C995,335 860,335 860,300" class="arrow"/>

  <rect x="20" y="580" width="1160" height="100" rx="8" class="state"/>
  <text x="35" y="612" class="head">Per-port health once each second</text>
  <text x="35" y="646">Good, bad, wrong-half, lost, restarts, silent-at-restart, duplicates, bytes in, last receive time, buffer records/bytes/losses.</text>

  <text x="30" y="730" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="752" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="774" class="small">Source: input.md.</text>
</svg>
```

The root box rejects corrupt, malformed or wrongly routed frames before checking continuity.  
Duplicates are dropped, gaps and restarts are counted, and accepted frames receive a timestamp and quality byte.  
Source: `input.md`.

## Level 3D — Root-box network stop and replay sequence

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-labelledby="l3r2-title">
  <title id="l3r2-title">Level 3 root network buffering sequence</title>
  <defs>
    <marker id="l3r2-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .state{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.event{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .done{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l3r2-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 3D — L3-R2 ROOT_NETWORK_BUFFER</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="30" y="140" width="200" height="145" rx="12" class="done"/>
  <text x="130" y="175" text-anchor="middle" class="head">ONLINE_EMPTY</text>
  <text x="130" y="209" text-anchor="middle">Network up</text>
  <text x="130" y="237" text-anchor="middle">buffer empty</text>
  <text x="130" y="265" text-anchor="middle">publish at once</text>

  <rect x="280" y="140" width="190" height="145" rx="12" class="event"/>
  <text x="375" y="175" text-anchor="middle" class="head">NETWORK_STOP</text>
  <text x="375" y="209" text-anchor="middle">Publish unavailable</text>
  <text x="375" y="237" text-anchor="middle">Keep message order</text>
  <text x="375" y="265" text-anchor="middle">on disk</text>

  <rect x="520" y="120" width="220" height="185" rx="12" class="event"/>
  <text x="630" y="155" text-anchor="middle" class="head">BUFFER_APPEND</text>
  <text x="630" y="189" text-anchor="middle">Append-only segment</text>
  <text x="630" y="217" text-anchor="middle">Length-prefixed record</text>
  <text x="630" y="245" text-anchor="middle">24 h start setting</text>
  <text x="630" y="273" text-anchor="middle">1 | 72 | 720 h alternatives</text>
  <text x="630" y="297" text-anchor="middle">4,096 MB cap</text>

  <rect x="800" y="120" width="230" height="185" rx="12" class="event"/>
  <text x="915" y="155" text-anchor="middle" class="head">CAP_ENFORCE</text>
  <text x="915" y="189" text-anchor="middle">If cap reached:</text>
  <text x="915" y="217" text-anchor="middle">remove oldest segment</text>
  <text x="915" y="245" text-anchor="middle">count its records lost</text>
  <text x="915" y="273" text-anchor="middle">never discard silently</text>

  <line x1="230" y1="212" x2="280" y2="212" class="arrow"/>
  <line x1="470" y1="212" x2="520" y2="212" class="arrow"/>
  <line x1="740" y1="212" x2="800" y2="212" class="arrow"/>

  <rect x="230" y="415" width="210" height="145" rx="12" class="done"/>
  <text x="335" y="450" text-anchor="middle" class="head">NETWORK_BACK</text>
  <text x="335" y="484" text-anchor="middle">Begin with oldest</text>
  <text x="335" y="512" text-anchor="middle">buffered message</text>
  <text x="335" y="540" text-anchor="middle">Keep order</text>

  <rect x="500" y="395" width="260" height="185" rx="12" class="done"/>
  <text x="630" y="430" text-anchor="middle" class="head">REPLAY_OLDEST</text>
  <text x="630" y="464" text-anchor="middle">Set quality bit 4</text>
  <text x="630" y="492" text-anchor="middle">Publish MQTT QoS 1</text>
  <text x="630" y="520" text-anchor="middle">Continue oldest first</text>
  <text x="630" y="548" text-anchor="middle">until empty</text>

  <rect x="820" y="415" width="260" height="145" rx="12" class="event"/>
  <text x="950" y="450" text-anchor="middle" class="head">REPLAY_INTERRUPTED</text>
  <text x="950" y="484" text-anchor="middle">Network drops again</text>
  <text x="950" y="512" text-anchor="middle">Keep the rest</text>
  <text x="950" y="540" text-anchor="middle">in order</text>

  <path d="M630,305 C630,355 335,355 335,415" class="arrow"/>
  <line x1="440" y1="487" x2="500" y2="487" class="arrow"/>
  <line x1="760" y1="487" x2="820" y2="487" class="arrow"/>
  <path d="M630,395 C630,345 130,345 130,285" class="arrow"/>
  <path d="M950,415 C950,350 630,350 630,305" class="arrow"/>

  <text x="30" y="655" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="677" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="699" class="small">Source: input.md. Buffer rate stated: about 89 MB/h for two halves and 178 MB/h for four halves.</text>
</svg>
```

A network stop redirects accepted messages into ordered, append-only disk segments.  
When the network returns, the root box marks buffered messages and replays them oldest first without losing the remaining order.  
Source: `input.md`.

## Level 3E — Logger storage, ordering and sample time

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 830" role="img" aria-labelledby="l3l1-title">
  <title id="l3l1-title">Level 3 logger ingestion ordering and timing</title>
  <defs>
    <marker id="l3l1-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .state{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.event{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .store{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l3l1-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 3E — L3-L1 LOGGER_INGEST</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="130" width="170" height="155" rx="12" class="state"/>
  <text x="105" y="165" text-anchor="middle" class="head">RAW_RECEIVE</text>
  <text x="105" y="199" text-anchor="middle">1,238-byte</text>
  <text x="105" y="227" text-anchor="middle">raw payload</text>
  <text x="105" y="255" text-anchor="middle">per frame</text>

  <rect x="225" y="110" width="210" height="195" rx="12" class="store"/>
  <text x="330" y="145" text-anchor="middle" class="head">STORE_AS_RECEIVED</text>
  <text x="330" y="179" text-anchor="middle">u32 length</text>
  <text x="330" y="207" text-anchor="middle">plus payload</text>
  <text x="330" y="235" text-anchor="middle">1,242-byte record</text>
  <text x="330" y="269" text-anchor="middle">Before processing</text>
  <text x="330" y="297" text-anchor="middle">Never replaced</text>

  <rect x="470" y="110" width="200" height="195" rx="12" class="state"/>
  <text x="570" y="145" text-anchor="middle" class="head">INDEX_MESSAGE</text>
  <text x="570" y="179" text-anchor="middle">Location and length</text>
  <text x="570" y="207" text-anchor="middle">Identity, boot, index</text>
  <text x="570" y="235" text-anchor="middle">samples, times</text>
  <text x="570" y="263" text-anchor="middle">and quality</text>

  <rect x="705" y="110" width="215" height="195" rx="12" class="state"/>
  <text x="812" y="145" text-anchor="middle" class="head">ORDER_BY_BOOT_INDEX</text>
  <text x="812" y="179" text-anchor="middle">Per half</text>
  <text x="812" y="207" text-anchor="middle">Hold up to 50 frames</text>
  <text x="812" y="235" text-anchor="middle">while waiting</text>
  <text x="812" y="263" text-anchor="middle">New boot = restart</text>

  <rect x="955" y="110" width="225" height="195" rx="12" class="state"/>
  <text x="1067" y="145" text-anchor="middle" class="head">MAP_SAMPLE_TIME</text>
  <text x="1067" y="179" text-anchor="middle">Latch and fraction</text>
  <text x="1067" y="207" text-anchor="middle">divided by line rate</text>
  <text x="1067" y="235" text-anchor="middle">plus filter delay</text>
  <text x="1067" y="263" text-anchor="middle">Receive time selects</text>
  <text x="1067" y="291" text-anchor="middle">whole edge second</text>

  <line x1="190" y1="207" x2="225" y2="207" class="arrow"/>
  <line x1="435" y1="207" x2="470" y2="207" class="arrow"/>
  <line x1="670" y1="207" x2="705" y2="207" class="arrow"/>
  <line x1="920" y1="207" x2="955" y2="207" class="arrow"/>

  <rect x="235" y="420" width="240" height="145" rx="12" class="event"/>
  <text x="355" y="455" text-anchor="middle" class="head">WAIT_FOR_MISSING</text>
  <text x="355" y="489" text-anchor="middle">Keep at most</text>
  <text x="355" y="517" text-anchor="middle">50 later frames</text>
  <text x="355" y="545" text-anchor="middle">for this half</text>

  <rect x="555" y="420" width="235" height="145" rx="12" class="event"/>
  <text x="672" y="455" text-anchor="middle" class="head">COUNT_LOGGER_GAP</text>
  <text x="672" y="489" text-anchor="middle">Missing frame</text>
  <text x="672" y="517" text-anchor="middle">did not arrive</text>
  <text x="672" y="545" text-anchor="middle">Count lost and continue</text>

  <rect x="870" y="420" width="235" height="145" rx="12" class="event"/>
  <text x="987" y="455" text-anchor="middle" class="head">LOGGER_RESTART</text>
  <text x="987" y="489" text-anchor="middle">Different boot count</text>
  <text x="987" y="517" text-anchor="middle">starts a new order</text>
  <text x="987" y="545" text-anchor="middle">for that half</text>

  <path d="M780,305 C780,360 355,360 355,420" class="arrow"/>
  <line x1="475" y1="492" x2="555" y2="492" class="arrow"/>
  <path d="M850,305 C850,360 987,360 987,420" class="arrow"/>
  <path d="M790,492 C850,492 850,350 1030,305" class="arrow"/>

  <text x="30" y="655" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="677" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="699" class="small">Source: input.md. The exact whole-second association and numeric filter delay are not specified.</text>
</svg>
```

The logger saves a raw message before attempting to order or interpret it.  
It waits through a limited reordering window, counts unresolved gaps and maps sample indexes to the 1 Hz reference.  
Source: `input.md`; exact whole-second selection and filter-delay values are not supplied.

## Level 3F — Logger movement, runs, position and results

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 860" role="img" aria-labelledby="l3l2-title">
  <title id="l3l2-title">Level 3 logger run processing sequence</title>
  <defs>
    <marker id="l3l2-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#315d7d"/>
    </marker>
  </defs>
  <style>
    text{font-family:sans-serif;font-size:16px;fill:#17212b}
    .title{font-size:24px;font-weight:700}.head{font-size:18px;font-weight:700}.small{font-size:14px}
    .state{fill:#eaf3fb;stroke:#315d7d;stroke-width:2}.event{fill:#fff3cd;stroke:#8a6d1d;stroke-width:2}
    .store{fill:#e8f5e9;stroke:#3d7750;stroke-width:2}
    .arrow{stroke:#315d7d;stroke-width:2.5;fill:none;marker-end:url(#l3l2-arrow)}
  </style>

  <text x="30" y="35" class="title">Level 3F — L3-L2 LOGGER_RUN_PROCESS</text>
  <text x="1170" y="35" text-anchor="end" class="small">Every label and number: input.md</text>

  <rect x="20" y="115" width="180" height="185" rx="12" class="state"/>
  <text x="110" y="150" text-anchor="middle" class="head">ONE_SECOND_WINDOW</text>
  <text x="110" y="184" text-anchor="middle">Running mean over</text>
  <text x="110" y="212" text-anchor="middle">one mains period</text>
  <text x="110" y="240" text-anchor="middle">Remove mean</text>
  <text x="110" y="268" text-anchor="middle">and slope</text>

  <rect x="235" y="115" width="200" height="185" rx="12" class="state"/>
  <text x="335" y="150" text-anchor="middle" class="head">MOVEMENT_SCORE</text>
  <text x="335" y="184" text-anchor="middle">RMS in strand-</text>
  <text x="335" y="212" text-anchor="middle">ripple band</text>
  <text x="335" y="240" text-anchor="middle">for each channel</text>
  <text x="335" y="268" text-anchor="middle">take channel median</text>

  <rect x="470" y="95" width="210" height="225" rx="12" class="event"/>
  <text x="575" y="130" text-anchor="middle" class="head">MOVING_STATE</text>
  <text x="575" y="164" text-anchor="middle">Above threshold</text>
  <text x="575" y="192" text-anchor="middle">for 2 s: moving</text>
  <text x="575" y="226" text-anchor="middle">Below threshold</text>
  <text x="575" y="254" text-anchor="middle">for 10 s: stopped</text>
  <text x="575" y="288" text-anchor="middle">Data-derived state</text>

  <rect x="715" y="95" width="205" height="225" rx="12" class="event"/>
  <text x="817" y="130" text-anchor="middle" class="head">SESSION_PADDING</text>
  <text x="817" y="164" text-anchor="middle">Keep 30 s before</text>
  <text x="817" y="192" text-anchor="middle">and 30 s after</text>
  <text x="817" y="226" text-anchor="middle">Stop shorter than</text>
  <text x="817" y="254" text-anchor="middle">75 s stays in</text>
  <text x="817" y="282" text-anchor="middle">one run</text>

  <rect x="955" y="115" width="225" height="185" rx="12" class="state"/>
  <text x="1067" y="150" text-anchor="middle" class="head">POSITION_AND_REGISTER</text>
  <text x="1067" y="184" text-anchor="middle">Count strand ripple</text>
  <text x="1067" y="212" text-anchor="middle">ramps + fixed length</text>
  <text x="1067" y="240" text-anchor="middle">Later run to first</text>
  <text x="1067" y="268" text-anchor="middle">within half a pitch</text>

  <line x1="200" y1="207" x2="235" y2="207" class="arrow"/>
  <line x1="435" y1="207" x2="470" y2="207" class="arrow"/>
  <line x1="680" y1="207" x2="715" y2="207" class="arrow"/>
  <line x1="920" y1="207" x2="955" y2="207" class="arrow"/>

  <rect x="250" y="430" width="300" height="180" rx="12" class="state"/>
  <text x="400" y="465" text-anchor="middle" class="head">ANALYSE_RUN</text>
  <text x="400" y="499" text-anchor="middle">312 mm level trace and drift</text>
  <text x="400" y="527" text-anchor="middle">Temperature correction</text>
  <text x="400" y="555" text-anchor="middle">Radial peaks above threshold</text>
  <text x="400" y="583" text-anchor="middle">Use frame temperatures</text>

  <rect x="650" y="410" width="310" height="220" rx="12" class="store"/>
  <text x="805" y="445" text-anchor="middle" class="head">WRITE_RUN_FILES</text>
  <text x="805" y="479" text-anchor="middle">Raw frames per half</text>
  <text x="805" y="507" text-anchor="middle">Index per half</text>
  <text x="805" y="535" text-anchor="middle">Run description</text>
  <text x="805" y="563" text-anchor="middle">Results</text>
  <text x="805" y="597" text-anchor="middle">Raw remains beside results</text>

  <path d="M1067,300 C1067,360 400,360 400,430" class="arrow"/>
  <line x1="550" y1="520" x2="650" y2="520" class="arrow"/>

  <text x="30" y="665">Both installations: proximity switches at both ends of fixed travel.</text>
  <text x="30" y="691">First installation: no plant-control connection; movement and position come from its own data.</text>
  <text x="30" y="735" class="small">Counts — half: 16 sensing elements, 16 channels; SWS = head = 2 halves; large winch: 2 SWS = 4 halves, 1 root box.</text>
  <text x="30" y="757" class="small">Large: 51 winches = 102 SWS = 204 halves, 51 root boxes. First: 6 winches = 6 SWS = 12 halves, 6 root boxes.</text>
  <text x="30" y="779" class="small">Source: input.md. Thresholds, band limits, mains period and position constants are not numerically specified.</text>
</svg>
```

One-second windows produce a movement score, and timed threshold crossings divide each head session into runs.  
Strand ripple then supplies position and registration before the logger writes raw data, indexes, descriptions and results.  
Source: `input.md`; several processing constants are intentionally unspecified.

# Level 4 — Pseudocode

All pseudocode facts and known data sizes come from `input.md`. Types marked `<?>` have no size or representation specified there.

### L3-H1 `HALF_ACQUIRE`

```text
type i24 = signed 3-byte integer; type i16 = signed 2-byte integer
type u16 = unsigned 2-byte integer; u32 = unsigned 4-byte integer
type u64 = unsigned 8-byte integer; SampleSet = i24[16]
state result_index:u64, line_index:u32, fill_count:u8, n:integer
state edge_pending:bool, pending_result:u64, latch:u32, fraction:u16
state cic_integrator:u64[16][3], cic_comb_delay:u64[16][3]
state block_sum:integer[16], correction_history:integer[16][2]

CAPTURE_EDGE:
    edge_pending = true; pending_result = result_index

FILTER_RESULT(x:SampleSet, optional temperatures:i16[2]):
    result_index += 1
    if filter_id == THREE_STAGE:
        for channel 0..15: update three wrapping u64 integrators with x[channel]
    else if filter_id == BLOCK:
        for channel 0..15: block_sum[channel] += x[channel]
    if result_index is not the configured n-th result: return no frame

DECIMATE:
    if filter_id == THREE_STAGE:
        for channel 0..15: y[channel] = THREE_COMBS(channel)
        for channel 0..15: y[channel] = (y[channel] + n^3/2) / n^3
    else:
        for channel 0..15: y[channel] = (block_sum[channel] + n/2) / n
        clear block_sum

APPLY_PENDING_EDGE:
    if edge_pending: (latch, fraction) = MAP_CAPTURE_TO_LINE_POSITION(pending_result)
    if edge_pending: edge_pending = false; edges_seen += 1

CORRECT_AND_CLAMP:
    if filter_id == THREE_STAGE:
        out = (-y[k] + 10*y[k-1] - y[k-2] + 4) >> 3 for every channel
    else: out = y
    clamp every out to [-2^23, 2^23 - 1]

PACK_LINE_SAMPLE:
    pack 16 out values as little-endian signed 24-bit; line_index += 1
    fill_count += 1; if fill_count == 25: invoke COMPLETE_FRAME
```

### L3-H2 `HALF_FRAME_AND_RESTART`

```text
type byte = u8; Frame = byte[1229]; Header = byte[25]
state fill:Frame, finished:Frame, boot_count:u8, frame_count:integer
state first_after_boot:bool, send_overflow:bool, send_busy:bool

COMPLETE_FRAME:
    fill[0] = 0x11; fill[1] = half_id
    put_u32_le(fill[2..5], first_sample_index)
    fill[6] = 25
    fill[7] = (filter_id << 6) | (converter_rate_code << 3) | line_rate_code
    put_u16_le(fill[8..9], first_after_boot_bit | send_overflow_bit)
    fill[10] = boot_count; fill[11] = edges_seen
    put_u32_le(fill[12..15], latch); put_u16_le(fill[16..17], fraction)
    put_i16_le(fill[18..19], temperature_1)
    put_i16_le(fill[20..21], temperature_2)
    fill[22] = low_byte(frame_count); put_u16_le(fill[23..24], aux_value)
    keep packed samples in fill[25..1224]
    put_u32_le(fill[1225..1228], CRC32C(fill[0..1224], 0x82F63B78))
    first_after_boot = false; frame_count += 1

SWAP_BUFFERS:
    swap(fill, finished); begin filling the now-free buffer

SEND_AVAILABLE:
    if send_busy: DROP_AND_LATCH_OVERFLOW; return
    COBS_SEND(COBS_ENCODE(finished) followed by byte 0x00 using 8N1)

DROP_AND_LATCH_OVERFLOW:
    drop finished; send_overflow = true

RESTART:
    increment boot_count; reset counters, filters, latch and filling frame
    send_overflow = false; first_after_boot = true; remain silent about 2 s
```

### L3-R1 `ROOT_ACCEPT_FRAME`

```text
type byte = u8; Frame = byte[1229]; StampedMessage = byte[1238]
type u32 = unsigned 4-byte integer; u64 = unsigned 8-byte integer
state last_boot:u8, last_first:u32, last_samples:u8, have_last:bool
state quality:u8; counters = good, bad, wrong_half, lost, restarts, duplicates

WAIT_DELIMITER:
    encoded = read bytes through the next 0x00 delimiter

DECODE_AND_CHECK:
    frame = COBS_DECODE(encoded without delimiter)
    if length(frame) != 1229 or CRC32C_INVALID(frame): bad += 1; drop
    if frame[0] != 0x11: bad += 1; drop
    if frame[1] != configured_half_id_for_port: wrong_half += 1; drop

CHECK_CONTINUITY:
    quality = 0
    boot = frame[10]; first = get_u32_le(frame[2..5]); samples = frame[6]
    if have_last and boot != last_boot:
        restarts += 1; estimate and count silent frames; quality |= 2
    else if have_last and first < last_first + last_samples:
        duplicates += 1; drop
    else if have_last and first > last_first + last_samples:
        gap = first - (last_first + last_samples)
        lost += gap / samples; quality |= 1

STAMP_AND_APPEND_9:
    message[0..1228] = frame unchanged
    put_u64_le(message[1229..1236], receive_microseconds_since_box_epoch)
    message[1237] = quality; good += 1
    last_boot = boot; last_first = first; last_samples = samples; have_last = true

ROUTE_MESSAGE:
    publish immediately only if network is up and disk buffer is empty
    otherwise invoke BUFFER_APPEND(message)
```

### L3-R2 `ROOT_NETWORK_BUFFER`

```text
type byte = u8; StampedMessage = byte[1238]
type BufferRecord = length-prefixed StampedMessage
# The buffer length-prefix size is not specified in input.md.
state network_up:bool, buffered_records:integer, buffered_bytes:integer
constant cap_bytes = 4096 MB; configured_hours = 24 | 1 | 72 | 720

ONLINE_EMPTY(message):
    if network_up and buffered_records == 0:
        publish message with MQTT QoS 1; return
    BUFFER_APPEND(message)

NETWORK_STOP:
    network_up = false

BUFFER_APPEND(message):
    append message in order to the current append-only segment
    increment buffered_records and buffered_bytes
    CAP_ENFORCE()

CAP_ENFORCE:
    while buffered_bytes reaches the cap:
        remove the oldest complete segment
        count every record in that segment as a buffer loss

NETWORK_BACK:
    network_up = true
    while network_up and buffered_records > 0:
        REPLAY_OLDEST()

REPLAY_OLDEST:
    message = oldest buffered message
    message.quality |= 4
    publish message with MQTT QoS 1
    if publish succeeds: remove that record and continue oldest first
    else: REPLAY_INTERRUPTED()

REPLAY_INTERRUPTED:
    network_up = false
    keep this and all remaining records in their existing order
```

### L3-L1 `LOGGER_INGEST`

```text
type byte = u8; RawMessage = byte[1238]
type StoredRecord = u32_length_prefix + RawMessage
type u8 = unsigned 1-byte; u16 = unsigned 2-byte
type u32 = unsigned 4-byte; u64 = unsigned 8-byte
state reorder_queue:ordered frames per half, maximum wait = 50 frames

RAW_RECEIVE(message:RawMessage):
    STORE_AS_RECEIVED(message)
    fields = INDEX_MESSAGE(message)
    ORDER_BY_BOOT_INDEX(fields, message)

STORE_AS_RECEIVED:
    offset = append u32(1238) followed by all 1238 message bytes

INDEX_MESSAGE:
    read half_id:u8, boot:u8, first_index:u32 and samples:u8
    read latch:u32, fraction:u16, receive_time:u64 and quality:u8
    create index row with offset, length, identity fields and these values

ORDER_BY_BOOT_INDEX:
    order per half by (boot, first_index)
    if boot differs from current boot: LOGGER_RESTART
    if the next expected frame is absent: WAIT_FOR_MISSING
    otherwise release consecutive frames to MAP_SAMPLE_TIME

WAIT_FOR_MISSING:
    hold up to 50 later frames for this half
    if the missing frame still has not arrived: COUNT_LOGGER_GAP

COUNT_LOGGER_GAP:
    count the missing range as lost and continue with the next held frame

MAP_SAMPLE_TIME:
    choose the edge's whole second using receive_time
    relative = (sample_index - latch - fraction/65536) / line_rate
    sample_time = chosen_edge_second + relative + filter_delay
    store the first sample's time in the message index
```

### L3-L2 `LOGGER_RUN_PROCESS`

```text
type Number<?> = numeric representation not specified in input.md
type Window = 1 second of ordered, timed values for one head
state movement_score:Number<?>, moving:bool, above_seconds:integer
state below_seconds:integer, session and run collections

ONE_SECOND_WINDOW(window:Window):
    subtract a running mean over one mains period
    remove the window mean and slope
    MOVEMENT_SCORE(window)

MOVEMENT_SCORE:
    for every channel: compute RMS in the strand-ripple band
    movement_score = median of the channel RMS values
    MOVING_STATE(movement_score)

MOVING_STATE:
    if score is above threshold: above_seconds += 1; below_seconds = 0
    if score is below threshold: below_seconds += 1; above_seconds = 0
    if above_seconds >= 2: moving = true
    if below_seconds >= 10: moving = false
    retain 30 seconds before and after detected movement

SESSION_PADDING:
    if a stopped interval is shorter than 75 seconds: keep one run
    otherwise close the run and begin a later run

POSITION_AND_REGISTER:
    derive position from strand-ripple counts, ramps and known fixed length
    register every later run to the first within half a strand pitch

ANALYSE_RUN:
    calculate a level trace over a 312 mm window and calculate drift
    apply temperature correction from frame temperatures
    list radial peaks above the configured threshold

WRITE_RUN_FILES:
    write raw frames and an index for each half
    write the run description and results beside the retained raw frames
```

# Arithmetic behind Level 0

All inputs below are from `input.md`; calculated results are identified as such.

- Frame frequency: `1,000 ms / 100 ms = 10 frames/s` per half (calc).
- Values per frame: `25 samples × 16 channels = 400 values` (calc).
- Values per half per second: `400 × 10 = 4,000`, also `16 × 250 = 4,000` (calc).
- Value bytes per frame: `25 × 16 × 3 = 1,200` (given and calc).
- Complete frame: `25-byte header + 1,200 values + 4-byte CRC = 1,229 bytes`.
- Unencoded frames: `1,229 × 10 = 12,290 B/s` per half (calc).
- Approximate COBS contribution: `ceil(1,229 / 254) = 5` bytes/frame, plus one `00h` delimiter (calc from the stated approximation).
- Approximate encoded serial rate: `(1,229 + 5 + 1) × 10 = 12,350 B/s` per half (calc).
- 8N1 wire rate used by those frames: `12,350 × 10 = 123,500 bit/s` per half (calc), within either named `460.8 kbit/s` or `1 Mbit/s` line-rate alternative.
- Root addition: `8-byte receive time + 1-byte quality = 9 bytes`.
- Raw MQTT payload: `(1,229 + 9) × 10 = 12,380 B/s` per half (calc).
- Logger record: `(4-byte length + 1,238-byte message) × 10 = 12,420 B/s` per half (calc).
- Calculated logger storage: `12,420 × 3,600 = 44,712,000 bytes/hour = 44.712 decimal MB/hour`; `input.md` states about `44.6 MB/hour`.

Scaling the 250-rate case:

| Unit | Halves | Values/s | Encoded serial B/s | Raw MQTT B/s | Logger-record B/s |
|---|---:|---:|---:|---:|---:|
| Half | 1 | 4,000 | ≈12,350 | 12,380 | 12,420 |
| SWS or first-installation winch | 2 | 8,000 | ≈24,700 | 24,760 | 24,840 |
| Large-installation winch/root box | 4 | 16,000 | ≈49,400 | 49,520 | 49,680 |
| First installation | 12 | 48,000 | ≈148,200 | 148,560 | 149,040 |
| Large installation | 204 | 816,000 | ≈2,519,400 | 2,525,520 | 2,533,680 |

Count arithmetic:

- Large installation: `51 winches × 2 SWS = 102 SWS`; `51 × 4 halves = 204 halves`; one box per winch gives `51 root boxes` (calc).
- First installation: `6 winches × 1 SWS = 6 SWS`; `6 × 2 halves = 12 halves`; one box per winch gives `6 root boxes` (calc).
- Stated buffer totals: `6 × 89 = 534 MB/hour` for the first installation and `51 × 178 = 9,078 MB/hour` for the large installation (calc).
- Raw-payload calculations instead give `148,560 × 3,600 = 534.816 MB/hour` and `2,525,520 × 3,600 = 9,091.872 MB/hour` in decimal MB (calc).
- Alternative line rates give `16 × 80 = 1,280`, `16 × 100 = 1,600`, and `16 × 125 = 2,000 values/s/half` (calc). Their complete framed B/s cannot be determined without a changed frame size or cadence.

# Possible inconsistencies

All compared facts are from `input.md`.

1. A frame every `100 ms` containing `25` samples implies exactly `250 samples/s/channel`. The alternatives `80`, `100` and `125` need a different frame cadence or sample count, but neither is specified.
2. The explicit logger record arithmetic gives `44.712 decimal MB/hour`, which would normally round to `44.7`, while the stated figure is about `44.6 MB/hour`.
3. A four-half box at the stated `178 MB/hour` needs `4,272 MB` for `24 h`, exceeding the `4,096 MB` cap. The cap holds about `4,096 / 178 = 23.0 h` (calc).
4. The half description names one digital temperature part, while the frame contains two temperature values. The origin of the second value is not explained.
5. The requested Level 2 wording says “time and alignment” inside the root box, but the root box is also explicitly said to perform no signal processing. I therefore showed it stamping and carrying alignment metadata; actual sample-time alignment remains in the logger.
6. The system design says the root box sends the 1 Hz edge, but real root-box edge output and clock discipline are explicitly listed as not built.

# What I could not check

- No implementation source is included in `input.md`, so the prototype behavior, byte-identical C implementation and “not built” status cannot be independently verified.
- MQTT topic, QoS, TCP and Ethernet overhead; health-text size; status-message size; and reverse serial traffic are unspecified. Therefore complete network and reverse-direction B/s cannot be calculated.
- Exact COBS output varies with frame contents; Level 0 uses only the stated approximation of about one byte per 254 plus a delimiter.
- Alternative line-rate framing and shared RS-485 polling overhead are unspecified.
- The root-buffer length-prefix size and segment-file overhead are unspecified.
- The exact edge-capture-to-fraction conversion, whole-second association and numeric filter delay are unspecified.
- Mains period, strand-ripple band, detection thresholds, strand pitch, fixed travel length, position algorithm details and temperature-correction formula are unspecified.
- Boot-count behavior after the `u8` value reaches its maximum is unspecified.
