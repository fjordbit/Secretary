---
kind: "model-round"
round: "2026-11-20-sol"
backend: "cursor"
model: "gpt-5.6-sol-xhigh"
model_used: "gpt-5.6-sol-xhigh"
label: "GPT 5.6 Sol, extra high (Cursor)"
status: "ok"
started: "2026-11-20T11:11:40+01:00"
finished: "2026-11-20T11:13:59+01:00"
seconds: 138.3
dry_run: false
input_sha256: "0ea5df21d939be5a81e92cef64f3ce25fd5f8a95a4206d734fc55f0af53e9597"
input_bytes: 6916
workdir: "~\\AppData\\Local\\Temp\\model-round-work\\round_20261120-111139\\work_cursor_l500m7yw"
command: ["~\\AppData\\Local\\cursor-agent\\agent.CMD", "-p", "--output-format", "text", "--mode", "ask", "--sandbox", "disabled", "--trust", "--workspace", "~\\AppData\\Local\\Temp\\model-round-work\\round_20261120-111139\\work_cursor_l500m7yw", "--model", "gpt-5.6-sol-xhigh", "The only file in this workspace is input.md. Read it and do exactly what it asks. Do not read or write anything else, do not run commands. Reply in Markdown."]
sent:
  - {"path": "brief", "bytes": 6349}
not_sent:
  []
---
Source key: **input.md** means the supplied brief. Arithmetic is derived from it. Outside assumptions are marked **(from memory)**.

## A. Whole line as blocks

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 610">
  <defs>
    <marker id="blueArrow" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto-start-reverse">
      <path d="M0,0 L6,3 L0,6 Z" fill="#2563a6"/>
    </marker>
    <marker id="orangeArrow" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#c55a11"/>
    </marker>
    <marker id="greyArrow" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#444"/>
    </marker>
  </defs>
  <style>
    text { font-family: sans-serif; font-size: 16px; fill: #17202a; }
    .title { font-size: 24px; font-weight: 700; }
    .head { font-size: 18px; font-weight: 700; }
    .small { font-size: 14px; }
    .box { fill: #f7f9fb; stroke: #34495e; stroke-width: 2; }
    .half { fill: #eaf2f8; stroke: #2563a6; stroke-width: 2; }
  </style>

  <rect width="1100" height="610" fill="white"/>
  <text x="40" y="38" class="title">One winch, two SWS, four separate half cables</text>

  <rect x="40" y="75" width="430" height="390" rx="10" class="box"/>
  <text x="60" y="105" class="head">Winch</text>

  <text x="65" y="145" class="head">Rope 1 — SWS 1</text>
  <rect x="80" y="165" width="150" height="58" rx="8" class="half"/>
  <rect x="80" y="245" width="150" height="58" rx="8" class="half"/>
  <text x="113" y="200">Half 1A</text>
  <text x="113" y="280">Half 1B</text>

  <text x="65" y="345" class="head">Rope 2 — SWS 2</text>
  <rect x="80" y="365" width="150" height="58" rx="8" class="half"/>
  <rect x="270" y="365" width="150" height="58" rx="8" class="half"/>
  <text x="113" y="400">Half 2A</text>
  <text x="303" y="400">Half 2B</text>

  <rect x="745" y="125" width="205" height="330" rx="10" class="box"/>
  <text x="805" y="158" class="head">Root box</text>
  <text x="765" y="198">Receives</text>
  <text x="765" y="226">Checks</text>
  <text x="765" y="254">Time-stamps</text>
  <text x="765" y="282">Buffers</text>
  <text x="765" y="310">Forwards</text>
  <text x="765" y="348" class="small">No signal processing</text>

  <g stroke-width="3" fill="none">
    <line x1="230" y1="188" x2="745" y2="188" stroke="#2563a6"
          marker-start="url(#blueArrow)" marker-end="url(#blueArrow)"/>
    <line x1="745" y1="198" x2="230" y2="198" stroke="#c55a11" marker-end="url(#orangeArrow)"/>
    <line x1="745" y1="208" x2="230" y2="208" stroke="#444" marker-end="url(#greyArrow)"/>

    <line x1="230" y1="268" x2="745" y2="268" stroke="#2563a6"
          marker-start="url(#blueArrow)" marker-end="url(#blueArrow)"/>
    <line x1="745" y1="278" x2="230" y2="278" stroke="#c55a11" marker-end="url(#orangeArrow)"/>
    <line x1="745" y1="288" x2="230" y2="288" stroke="#444" marker-end="url(#greyArrow)"/>

    <line x1="230" y1="388" x2="745" y2="388" stroke="#2563a6"
          marker-start="url(#blueArrow)" marker-end="url(#blueArrow)"/>
    <line x1="745" y1="398" x2="230" y2="398" stroke="#c55a11" marker-end="url(#orangeArrow)"/>
    <line x1="745" y1="408" x2="230" y2="408" stroke="#444" marker-end="url(#greyArrow)"/>

    <line x1="420" y1="388" x2="745" y2="388" stroke="#2563a6"
          marker-start="url(#blueArrow)" marker-end="url(#blueArrow)"/>
    <line x1="745" y1="398" x2="420" y2="398" stroke="#c55a11" marker-end="url(#orangeArrow)"/>
    <line x1="745" y1="408" x2="420" y2="408" stroke="#444" marker-end="url(#greyArrow)"/>
  </g>

  <text x="500" y="166" class="small">Each cable: about 5–100 m</text>

  <line x1="950" y1="290" x2="1000" y2="290" stroke="#2563a6" stroke-width="4"
        marker-end="url(#blueArrow)"/>
  <rect x="1000" y="240" width="85" height="100" rx="8" class="box"/>
  <text x="1009" y="280" class="head">Network</text>
  <text x="1015" y="310">to logger</text>

  <g transform="translate(45 500)">
    <line x1="0" y1="0" x2="70" y2="0" stroke="#2563a6" stroke-width="3"
          marker-start="url(#blueArrow)" marker-end="url(#blueArrow)"/>
    <text x="85" y="6">RS-422 data both ways: four wires</text>
    <line x1="410" y1="0" x2="480" y2="0" stroke="#c55a11" stroke-width="3"
          marker-end="url(#orangeArrow)"/>
    <text x="495" y="6">1 Hz edge down: dedicated differential pair</text>
    <line x1="0" y1="42" x2="70" y2="42" stroke="#444" stroke-width="3"
          marker-end="url(#greyArrow)"/>
    <text x="85" y="48">24 V supply down</text>
    <text x="410" y="48">Line rate: 460.8 kbit/s or 1 Mbit/s</text>
  </g>

  <text x="40" y="592" class="small">Source for topology, functions, distances and line contents: input.md.</text>
</svg>
```

Each Half has its own point-to-point cable to the root box.  
Frames travel up, while data, the 1 Hz edge and 24 V can travel down as shown.  
Source: input.md.

## B. Inside one Half

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680">
  <defs>
    <marker id="arrow2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#2563a6"/>
    </marker>
    <marker id="orange2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#c55a11"/>
    </marker>
  </defs>
  <style>
    text { font-family: sans-serif; font-size: 16px; fill: #17202a; }
    .title { font-size: 24px; font-weight: 700; }
    .head { font-size: 18px; font-weight: 700; }
    .small { font-size: 14px; }
    .box { fill: #f7f9fb; stroke: #34495e; stroke-width: 2; }
    .blue { fill: #eaf2f8; stroke: #2563a6; stroke-width: 2; }
    .orange { fill: #fff2e8; stroke: #c55a11; stroke-width: 2; }
    .flow { fill: none; stroke: #2563a6; stroke-width: 3; marker-end: url(#arrow2); }
    .clock { fill: none; stroke: #c55a11; stroke-width: 3; marker-end: url(#orange2); }
  </style>

  <rect width="1100" height="680" fill="white"/>
  <text x="40" y="38" class="title">Inside one Half: one local crystal</text>
  <rect x="35" y="65" width="1030" height="555" rx="12" class="box"/>

  <rect x="70" y="115" width="180" height="90" rx="8" class="blue"/>
  <text x="105" y="150" class="head">8 radial</text>
  <text x="89" y="178">sensing elements</text>

  <rect x="70" y="245" width="180" height="90" rx="8" class="blue"/>
  <text x="108" y="280" class="head">8 axial</text>
  <text x="89" y="308">sensing elements</text>

  <rect x="300" y="150" width="150" height="155" rx="8" class="box"/>
  <text x="322" y="185" class="head">16 analogue</text>
  <text x="340" y="214">paths</text>
  <text x="315" y="250" class="small">Allocation between</text>
  <text x="316" y="272" class="small">converters is not stated</text>

  <rect x="505" y="105" width="180" height="115" rx="8" class="blue"/>
  <text x="535" y="140" class="head">Converter A</text>
  <text x="548" y="170">8 channels</text>
  <text x="523" y="196" class="small">Simultaneous internally</text>

  <rect x="505" y="265" width="180" height="115" rx="8" class="blue"/>
  <text x="535" y="300" class="head">Converter B</text>
  <text x="548" y="330">8 channels</text>
  <text x="523" y="356" class="small">Simultaneous internally</text>

  <rect x="755" y="185" width="190" height="155" rx="8" class="blue"/>
  <text x="782" y="220" class="head">Microcontroller</text>
  <text x="780" y="250">Sample index</text>
  <text x="780" y="278">Averaging, if used</text>
  <text x="780" y="306">Frame assembly</text>

  <rect x="760" y="405" width="180" height="75" rx="8" class="box"/>
  <text x="795" y="437" class="head">Line driver</text>
  <text x="795" y="462">RS-422 cable</text>

  <rect x="505" y="425" width="180" height="70" rx="8" class="box"/>
  <text x="528" y="458" class="head">Digital temperature</text>
  <text x="568" y="480">part</text>

  <rect x="270" y="430" width="160" height="90" rx="45" class="orange"/>
  <text x="310" y="466" class="head">One crystal</text>
  <text x="300" y="493">up to ±40 ppm</text>

  <rect x="270" y="555" width="415" height="42" rx="6" class="orange"/>
  <text x="295" y="582">One common start-up synchronising pulse to both converters</text>

  <path d="M250 160 H300" class="flow"/>
  <path d="M250 290 H300" class="flow"/>
  <path d="M450 195 H505" class="flow"/>
  <path d="M450 265 H505" class="flow"/>
  <path d="M685 162 H720 V220 H755" class="flow"/>
  <path d="M685 322 H720 V285 H755" class="flow"/>
  <path d="M685 460 H720 V320 H755" class="flow"/>
  <path d="M850 340 V405" class="flow"/>

  <path d="M430 460 H470 V180 H505" class="clock"/>
  <path d="M470 320 H505" class="clock"/>
  <path d="M430 480 H735 V330 H755" class="clock" stroke-dasharray="8 7"/>
  <text x="447" y="445" class="small" fill="#c55a11">Clock input</text>
  <text x="525" y="515" class="small" fill="#c55a11">Proposed: same crystal drives MCU timer</text>

  <path d="M390 555 V235 H505" fill="none" stroke="#c55a11" stroke-width="2"/>
  <path d="M390 235 H480 V322 H505" fill="none" stroke="#c55a11" stroke-width="2"/>

  <path d="M1010 365 H945" class="clock"/>
  <text x="945" y="355" class="small">1 Hz edge:</text>
  <text x="945" y="378" class="small">latch index and</text>
  <text x="945" y="401" class="small">timer fraction</text>

  <text x="45" y="652" class="small">Source: input.md. Exact radial/axial allocation and sync-pulse source are not stated there.</text>
</svg>
```

The one crystal clocks both converter inputs and is proposed to clock the microcontroller timer.  
Both converters receive one common synchronising pulse at start-up and are not reset during a run.  
Source: input.md.

## C. RS-422 and shared four-wire RS-485

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 600">
  <style>
    text { font-family: sans-serif; font-size: 16px; fill: #17202a; }
    .title { font-size: 24px; font-weight: 700; }
    .head { font-size: 18px; font-weight: 700; }
    .small { font-size: 14px; }
    .box { fill: #f7f9fb; stroke: #34495e; stroke-width: 2; }
    .half { fill: #eaf2f8; stroke: #2563a6; stroke-width: 2; }
    .tx { stroke: #2563a6; stroke-width: 4; }
    .rx { stroke: #c55a11; stroke-width: 4; }
  </style>

  <rect width="1100" height="600" fill="white"/>
  <text x="40" y="38" class="title">Data wiring alternatives for four Halves</text>
  <line x1="550" y1="65" x2="550" y2="520" stroke="#aab2bd" stroke-width="2"/>

  <text x="90" y="85" class="head">RS-422: one root-box port per Half</text>
  <rect x="50" y="115" width="170" height="340" rx="10" class="box"/>
  <text x="91" y="145" class="head">Root box</text>

  <g>
    <rect x="78" y="170" width="115" height="45" rx="5" class="box"/><text x="109" y="198">Port 1</text>
    <rect x="78" y="235" width="115" height="45" rx="5" class="box"/><text x="109" y="263">Port 2</text>
    <rect x="78" y="300" width="115" height="45" rx="5" class="box"/><text x="109" y="328">Port 3</text>
    <rect x="78" y="365" width="115" height="45" rx="5" class="box"/><text x="109" y="393">Port 4</text>

    <rect x="410" y="170" width="100" height="45" rx="5" class="half"/><text x="434" y="198">Half 1</text>
    <rect x="410" y="235" width="100" height="45" rx="5" class="half"/><text x="434" y="263">Half 2</text>
    <rect x="410" y="300" width="100" height="45" rx="5" class="half"/><text x="434" y="328">Half 3</text>
    <rect x="410" y="365" width="100" height="45" rx="5" class="half"/><text x="434" y="393">Half 4</text>

    <line x1="193" y1="188" x2="410" y2="188" class="tx"/>
    <line x1="193" y1="202" x2="410" y2="202" class="rx"/>
    <line x1="193" y1="253" x2="410" y2="253" class="tx"/>
    <line x1="193" y1="267" x2="410" y2="267" class="rx"/>
    <line x1="193" y1="318" x2="410" y2="318" class="tx"/>
    <line x1="193" y1="332" x2="410" y2="332" class="rx"/>
    <line x1="193" y1="383" x2="410" y2="383" class="tx"/>
    <line x1="193" y1="397" x2="410" y2="397" class="rx"/>
  </g>
  <text x="85" y="485">4 ports × 4 data wires = 16 data conductors</text>

  <text x="620" y="85" class="head">Alternative: one shared four-wire RS-485 line</text>
  <rect x="600" y="115" width="170" height="115" rx="10" class="box"/>
  <text x="642" y="148" class="head">Root box</text>
  <text x="628" y="180">One shared port</text>
  <text x="625" y="207">TX pair + RX pair</text>

  <line x1="770" y1="165" x2="1020" y2="165" class="tx"/>
  <line x1="770" y1="190" x2="1020" y2="190" class="rx"/>

  <g>
    <line x1="820" y1="165" x2="820" y2="285" class="tx"/>
    <line x1="832" y1="190" x2="832" y2="285" class="rx"/>
    <rect x="780" y="285" width="105" height="50" rx="5" class="half"/><text x="803" y="316">Half 1</text>

    <line x1="900" y1="165" x2="900" y2="365" class="tx"/>
    <line x1="912" y1="190" x2="912" y2="365" class="rx"/>
    <rect x="860" y="365" width="105" height="50" rx="5" class="half"/><text x="883" y="396">Half 2</text>

    <line x1="980" y1="165" x2="980" y2="285" class="tx"/>
    <line x1="992" y1="190" x2="992" y2="285" class="rx"/>
    <rect x="940" y="285" width="105" height="50" rx="5" class="half"/><text x="963" y="316">Half 3</text>

    <line x1="730" y1="190" x2="730" y2="365" class="rx"/>
    <line x1="718" y1="165" x2="718" y2="365" class="tx"/>
    <rect x="675" y="365" width="105" height="50" rx="5" class="half"/><text x="698" y="396">Half 4</text>
  </g>
  <text x="640" y="485">One shared set of four data conductors</text>

  <line x1="60" y1="535" x2="120" y2="535" class="tx"/>
  <text x="130" y="541">Root-box-to-Half differential pair</text>
  <line x1="420" y1="535" x2="480" y2="535" class="rx"/>
  <text x="490" y="541">Half-to-root-box differential pair</text>
  <text x="40" y="578" class="small">Source: input.md. Edge pairs, supply wiring, RS-485 termination and bus access are not specified here.</text>
</svg>
```

RS-422 gives each Half its own four-wire data path and root-box port.  
The alternative connects all four Halves to one shared four-wire RS-485 line.  
Source: input.md; exact RS-485 termination and bus access are unspecified.

## D. Four local clocks and the 1 Hz latch

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700">
  <defs>
    <marker id="arrow4" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#2563a6"/>
    </marker>
  </defs>
  <style>
    text { font-family: sans-serif; font-size: 16px; fill: #17202a; }
    .title { font-size: 24px; font-weight: 700; }
    .head { font-size: 18px; font-weight: 700; }
    .small { font-size: 14px; }
    .axis { stroke: #34495e; stroke-width: 2; }
    .tick { stroke: #2563a6; stroke-width: 3; }
    .edge { stroke: #c55a11; stroke-width: 4; stroke-dasharray: 9 6; }
    .box { fill: #f7f9fb; stroke: #34495e; stroke-width: 2; }
    .orange { fill: #fff2e8; stroke: #c55a11; stroke-width: 2; }
  </style>

  <rect width="1100" height="700" fill="white"/>
  <text x="40" y="38" class="title">Local sample clocks anchored to one root-box time base</text>
  <text x="40" y="68" fill="#c55a11">Clock differences below are deliberately exaggerated; recorded maximum is 80 ppm between two Halves.</text>

  <line x1="455" y1="90" x2="455" y2="475" class="edge"/>
  <text x="370" y="105" class="head" fill="#c55a11">Root-box 1 Hz edge</text>

  <g>
    <text x="45" y="160" class="head">Half A crystal</text>
    <line x1="200" y1="155" x2="760" y2="155" class="axis"/>
    <path d="M220 135V175 M300 135V175 M380 135V175 M460 135V175 M540 135V175 M620 135V175 M700 135V175" class="tick"/>
    <circle cx="455" cy="155" r="7" fill="#c55a11"/>

    <text x="45" y="240" class="head">Half B crystal</text>
    <line x1="200" y1="235" x2="760" y2="235" class="axis"/>
    <path d="M215 215V255 M293 215V255 M371 215V255 M449 215V255 M527 215V255 M605 215V255 M683 215V255" class="tick"/>
    <circle cx="455" cy="235" r="7" fill="#c55a11"/>

    <text x="45" y="320" class="head">Half C crystal</text>
    <line x1="200" y1="315" x2="760" y2="315" class="axis"/>
    <path d="M225 295V335 M307 295V335 M389 295V335 M471 295V335 M553 295V335 M635 295V335 M717 295V335" class="tick"/>
    <circle cx="455" cy="315" r="7" fill="#c55a11"/>

    <text x="45" y="400" class="head">Half D crystal</text>
    <line x1="200" y1="395" x2="760" y2="395" class="axis"/>
    <path d="M210 375V415 M286 375V415 M362 375V415 M438 375V415 M514 375V415 M590 375V415 M666 375V415 M742 375V415" class="tick"/>
    <circle cx="455" cy="395" r="7" fill="#c55a11"/>
  </g>

  <rect x="790" y="115" width="260" height="310" rx="10" class="orange"/>
  <text x="815" y="150" class="head">Each Half latches</text>
  <text x="815" y="185">A: sample index N<tspan baseline-shift="sub">A</tspan> + fraction φ<tspan baseline-shift="sub">A</tspan></text>
  <text x="815" y="230">B: sample index N<tspan baseline-shift="sub">B</tspan> + fraction φ<tspan baseline-shift="sub">B</tspan></text>
  <text x="815" y="275">C: sample index N<tspan baseline-shift="sub">C</tspan> + fraction φ<tspan baseline-shift="sub">C</tspan></text>
  <text x="815" y="320">D: sample index N<tspan baseline-shift="sub">D</tspan> + fraction φ<tspan baseline-shift="sub">D</tspan></text>
  <text x="815" y="365" class="small">φ is measured by the timer</text>
  <text x="815" y="390" class="small">within one sample period.</text>

  <path d="M910 425 V480" stroke="#2563a6" stroke-width="3" fill="none" marker-end="url(#arrow4)"/>
  <rect x="150" y="480" width="850" height="145" rx="10" class="box"/>
  <text x="180" y="515" class="head">Root-box mapping</text>
  <text x="180" y="550">Known edge time + each reported latch → one index-to-time map for each Half</text>
  <text x="180" y="585">Per-Half maps → interpolation → values lined up on one common time base</text>
  <line x1="215" y1="605" x2="935" y2="605" class="axis"/>
  <path d="M280 595V615 M440 595V615 M600 595V615 M760 595V615 M920 595V615" class="tick"/>

  <text x="40" y="675" class="small">Source: input.md. Tick positions are illustrative symbols, not measured values.</text>
</svg>
```

Each Half samples continuously on its own crystal and reports where the 1 Hz edge arrived.  
The root box uses those latches to map all sample indices to one time base and interpolate.  
Source: input.md; the visible clock difference is deliberately exaggerated.

## E. Cable-length delay

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 720">
  <style>
    text { font-family: sans-serif; font-size: 16px; fill: #17202a; }
    .title { font-size: 24px; font-weight: 700; }
    .head { font-size: 18px; font-weight: 700; }
    .small { font-size: 14px; }
    .box { fill: #f7f9fb; stroke: #34495e; stroke-width: 2; }
    .orange { fill: #fff2e8; stroke: #c55a11; stroke-width: 2; }
    .blue { fill: #eaf2f8; stroke: #2563a6; stroke-width: 2; }
  </style>

  <rect width="1100" height="720" fill="white"/>
  <text x="40" y="38" class="title">Propagation offset from a 5 m cable and a 100 m cable</text>
  <rect x="40" y="65" width="1020" height="58" rx="8" class="orange"/>
  <text x="60" y="90">Assumption: twisted-pair velocity factor 0.66 and c = 299,792,458 m/s (from memory).</text>
  <text x="60" y="113">Calculated propagation: 5.05 ns per metre.</text>

  <text x="55" y="175" class="head">5 m cable</text>
  <rect x="175" y="150" width="45" height="34" fill="#2563a6"/>
  <text x="245" y="174">5 × 5.05 ns = 25.3 ns</text>

  <text x="55" y="235" class="head">100 m cable</text>
  <rect x="175" y="210" width="780" height="34" fill="#2563a6"/>
  <text x="700" y="270">100 × 5.05 ns = 505 ns</text>

  <rect x="55" y="305" width="990" height="80" rx="8" class="blue"/>
  <text x="75" y="338" class="head">Difference caused by the extra 95 m</text>
  <text x="75" y="367">95 × 5.05 ns = 480 ns = 0.480 µs = 0.000480 ms</text>

  <text x="55" y="430" class="head">Compared with the interval between values</text>
  <rect x="55" y="450" width="850" height="38" fill="#dfe6e9" stroke="#34495e"/>
  <text x="420" y="476">One interval at 250 values/s = 4 ms</text>
  <rect x="55" y="500" width="8" height="38" fill="#c55a11"/>
  <text x="80" y="526">Cable difference = 0.0120% of one interval; orange width is enlarged for visibility.</text>

  <rect x="55" y="570" width="480" height="92" rx="8" class="box"/>
  <text x="75" y="600" class="head">Rope movement during 0.480 µs</text>
  <text x="75" y="628">At 3.2 m/min: 0.0256 µm</text>
  <text x="75" y="652">At 5 m/min: 0.0400 µm</text>

  <rect x="565" y="570" width="480" height="92" rx="8" class="box"/>
  <text x="585" y="600" class="head">Rope movement during one 4 ms interval</text>
  <text x="585" y="628">At 3.2 m/min: 0.213 mm</text>
  <text x="585" y="652">At 5 m/min: 0.333 mm</text>

  <text x="40" y="700" class="small">Cable lengths, rates and rope speeds: input.md. Propagation assumptions: from memory. Values are derived.</text>
</svg>
```

With the stated memory-based propagation assumption, 95 m of extra cable adds about 0.480 µs.  
That is tiny beside the 4 ms between values and the corresponding rope movement.  
Sources: input.md for operating figures; velocity factor and c are from memory.

## F. Sampling-clock arrangements

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 720">
  <style>
    text { font-family: sans-serif; font-size: 16px; fill: #17202a; }
    .title { font-size: 24px; font-weight: 700; }
    .head { font-size: 18px; font-weight: 700; }
    .small { font-size: 14px; }
    .col { fill: #f7f9fb; stroke: #34495e; stroke-width: 2; }
    .blue { fill: #eaf2f8; stroke: #2563a6; stroke-width: 2; }
    .orange { fill: #fff2e8; stroke: #c55a11; stroke-width: 2; }
  </style>

  <rect width="1100" height="720" fill="white"/>
  <text x="40" y="38" class="title">Clock and timing-mark arrangements — alternatives, not a selection</text>

  <rect x="35" y="75" width="330" height="570" rx="10" class="col"/>
  <text x="60" y="110" class="head">Own crystal + edge</text>
  <rect x="60" y="135" width="280" height="70" rx="8" class="blue"/>
  <text x="80" y="165">4 Halves × 1 crystal</text>
  <text x="80" y="190" class="head">= 4 known sample crystals</text>
  <text x="60" y="245" class="head">Parts</text>
  <text x="60" y="274">One crystal per Half;</text>
  <text x="60" y="300">edge capture in each Half;</text>
  <text x="60" y="326">root edge distribution.</text>
  <text x="60" y="370" class="head">Wires</text>
  <text x="60" y="399">Dedicated edge pair in</text>
  <text x="60" y="425">each of four cables.</text>
  <text x="60" y="470" class="head">If the edge is lost</text>
  <text x="60" y="499">Sampling and frames continue,</text>
  <text x="60" y="525">but new common-time anchors stop.</text>
  <text x="60" y="551">Worst free drift can grow by</text>
  <text x="60" y="577">80 µs per second between Halves.</text>

  <rect x="385" y="75" width="330" height="570" rx="10" class="col"/>
  <text x="410" y="110" class="head">Clock sent from root box</text>
  <rect x="410" y="135" width="280" height="70" rx="8" class="orange"/>
  <text x="430" y="165">1 shared sample-clock source</text>
  <text x="430" y="190">at root; 0 independent Half clocks</text>
  <text x="410" y="245" class="head">Parts</text>
  <text x="410" y="274">One 2.048 or 4.096 MHz source;</text>
  <text x="410" y="300">distribution and reception;</text>
  <text x="410" y="326">local MCU clocks are unspecified.</text>
  <text x="410" y="370" class="head">Wires</text>
  <text x="410" y="399">Continuous clock uses the pair</text>
  <text x="410" y="425">to every Half.</text>
  <text x="410" y="470" class="head">If the clock is lost</text>
  <text x="410" y="499">Converters directly driven by it</text>
  <text x="410" y="525">cannot make new conversions.</text>
  <text x="410" y="551">Recovery behaviour is not stated.</text>

  <rect x="735" y="75" width="330" height="570" rx="10" class="col"/>
  <text x="760" y="110" class="head">Edge as a downlink byte</text>
  <rect x="760" y="135" width="280" height="70" rx="8" class="blue"/>
  <text x="780" y="165">4 Halves × 1 crystal</text>
  <text x="780" y="190" class="head">= 4 known sample crystals</text>
  <text x="760" y="245" class="head">Parts</text>
  <text x="760" y="274">Existing downlink carries the mark;</text>
  <text x="760" y="300">the start bit is the 1 Hz edge.</text>
  <text x="760" y="370" class="head">Wires</text>
  <text x="760" y="399">Dedicated pair is freed:</text>
  <text x="760" y="425">4 pairs = 8 conductors.</text>
  <text x="760" y="470" class="head">If the byte is lost</text>
  <text x="760" y="499">Sampling and frames continue,</text>
  <text x="760" y="525">but that common-time anchor is lost.</text>
  <text x="760" y="551">Further drift follows the same</text>
  <text x="760" y="577">free-running-clock behaviour.</text>

  <text x="40" y="675" class="small">Source: input.md; failure effects are direct consequences of the stated clock connections.</text>
  <text x="40" y="699" class="small">“One root crystal” is conditional: the brief specifies one shared clock source, not its physical implementation.</text>
</svg>
```

The recorded design and byte-edge alternative retain four independent Half crystals.  
The root-clock alternative has one functional sample-clock source, but its physical oscillator is unspecified.  
Source: input.md; no alternative is selected here.

## Numbers behind D, E and F

### D. Clock drift and 1 Hz correction

- Sample interval: \(1/250 = 0.004\text{ s} = 4\text{ ms}\). Source: input.md.
- One crystal’s recorded worst tolerance: \(20+20=40\text{ ppm}\). Source: input.md.
- Two crystals at opposite limits: \(40+40=80\text{ ppm}\). Source: input.md.
- Relative drift in one second: \(1\text{ s}\times80/1{,}000{,}000=80\,\mu\text{s}=0.080\text{ ms}\). Derived from input.md.
- This is \(0.080/1.0=8\%\) of the recorded 1.0 ms alignment requirement. Derived from input.md.
- At an ideal latch, oscillator phase error is removed at the anchor. With exact anchors and constant frequency error, interpolation between consecutive anchors also removes the linear drift. Actual residual depends on timer resolution, edge skew, jitter and within-second frequency change, none of which is given in input.md.
- If no later anchor were available and nominal rate alone were used, the worst tolerance-bound error would grow as \(80\,\mu\text{s}\times T\), reaching \(1\text{ ms}\) after \(1000/80=12.5\text{ s}\). Derived from input.md.
- Conditional ageing difference after one year at opposite limits: \(2+2=4\text{ ppm/year}\). Whether this should be added directly to the tolerance bound is not defined in input.md.

### E. Cable delay and rope movement

Propagation assumptions: velocity factor \(0.66\) and \(c=299{,}792{,}458\text{ m/s}\), both from memory.

- Velocity: \(0.66\times299{,}792{,}458=197{,}863{,}022\text{ m/s}\).
- Delay per metre: \(1/197{,}863{,}022=5.054\text{ ns/m}\).
- 5 m: \(5\times5.054=25.27\text{ ns}\).
- 100 m: \(100\times5.054=505.4\text{ ns}\).
- Difference: \((100-5)\times5.054=480.1\text{ ns}=0.4801\,\mu\text{s}\).
- Against one value interval: \(0.4801\,\mu\text{s}/4000\,\mu\text{s}\times100=0.0120\%\).
- At 3.2 m/min: \((3.2/60)\times0.4801\times10^{-6}=2.56\times10^{-8}\text{ m}=0.0256\,\mu\text{m}\).
- At 5 m/min: \((5/60)\times0.4801\times10^{-6}=4.00\times10^{-8}\text{ m}=0.0400\,\mu\text{m}\).
- Rope between values at 3.2 m/min: \((3.2/60)\times0.004=0.000213\text{ m}=0.213\text{ mm}\).
- Rope between values at 5 m/min: \((5/60)\times0.004=0.000333\text{ m}=0.333\text{ mm}\).

Cable lengths, sample rate and rope speeds come from input.md; all propagation-dependent results also use the memory-based assumptions above.

### F. Counts and wiring

- Recorded design: \(2\text{ SWS}\times2\text{ Halves/SWS}\times1\text{ crystal/Half}=4\) known sample-clock crystals. Derived from input.md.
- Root-clock alternative: one functional shared clock source and no independent Half converter-clock sources. Calling this exactly one physical crystal is conditional because input.md does not specify the source technology.
- Edge-as-byte alternative: the local clock arrangement is unchanged, so \(4\times1=4\) known Half crystals. Derived from input.md.
- Dedicated-edge wiring: \(4\text{ cables}\times1\text{ pair}=4\text{ pairs}=8\) conductors. The byte alternative frees these conductors. Derived from input.md.
- Point-to-point data wiring: \(4\text{ Halves}\times4\text{ wires}=16\) data conductors. Shared four-wire RS-485 uses one shared set of four data conductors. Derived from input.md.

## Short answers

**How many crystals?**  
The design on record has one crystal in each Half: two per SWS and four known sampling crystals for two SWS. Both converters in a Half share that crystal, and the microcontroller timer is proposed to share it. The edge-as-byte alternative does not change this. The root-clock alternative reduces the functional sampling-clock sources to one, but input.md does not establish whether that source—or other root-box and microcontroller clocks—is physically implemented with crystals.

**Does cable length or a start command create an offset?**  
Yes. Under the memory-based propagation assumption, a command reaches a 100 m cable about \(0.480\,\mu\text{s}\) later than a 5 m cable. That cable component is about 2,083 times smaller than the 1.0 ms requirement: \(1\text{ ms}/0.000480\text{ ms}\approx2083\).

A start command can also encounter launch, serial-reception and firmware scheduling differences that cannot be calculated from input.md. The common start-up synchronising pulse aligns the two converters inside one Half, not all four Halves. The recorded design instead uses the sample-index latches and 1 Hz marks to map independently started Halves onto one time base.

## What I could not check

- The actual cable velocity factor, construction and propagation variation.
- Timer frequency, capture resolution, edge jitter and distribution skew.
- Whether root-box software compensates for known cable lengths.
- Start-command launch skew, serial format and firmware response latency.
- Short-term crystal-frequency variation between 1 Hz marks.
- The physical oscillator and total crystal count in the root-clock alternative.
- Additional crystals needed by microcontrollers, communications or the root box.
- Radial and axial sensing-element allocation between the two converters.
- RS-485 termination, topology, addressing and bus-access rules.
- Clock-loss and edge-loss recovery behaviour.
