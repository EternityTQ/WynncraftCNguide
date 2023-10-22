import {
  flowRendererV2,
  flowStyles
} from "./chunk-QKHPZNRF.js";
import {
  flowDb,
  parser$1
} from "./chunk-BBAMAA7B.js";
import "./chunk-XIF57M4U.js";
import "./chunk-J6TH4YPY.js";
import "./chunk-NUDPJEUA.js";
import "./chunk-5NNWZHYY.js";
import "./chunk-3UOZPXZ3.js";
import "./chunk-R4IH42G5.js";
import {
  require_dayjs_min,
  require_dist,
  setConfig
} from "./chunk-ODF7ZWPD.js";
import {
  __toESM
} from "./chunk-2LSFTFF7.js";

// node_modules/mermaid/dist/flowDiagram-v2-58f49b84.js
var import_dayjs = __toESM(require_dayjs_min(), 1);
var import_sanitize_url = __toESM(require_dist(), 1);
var diagram = {
  parser: parser$1,
  db: flowDb,
  renderer: flowRendererV2,
  styles: flowStyles,
  init: (cnf) => {
    if (!cnf.flowchart) {
      cnf.flowchart = {};
    }
    cnf.flowchart.arrowMarkerAbsolute = cnf.arrowMarkerAbsolute;
    setConfig({ flowchart: { arrowMarkerAbsolute: cnf.arrowMarkerAbsolute } });
    flowRendererV2.setConf(cnf.flowchart);
    flowDb.clear();
    flowDb.setGen("gen-2");
  }
};
export {
  diagram
};
//# sourceMappingURL=flowDiagram-v2-58f49b84-7RTKFXJW.js.map
