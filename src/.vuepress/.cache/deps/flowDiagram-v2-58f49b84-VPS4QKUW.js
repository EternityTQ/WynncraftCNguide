import {
  flowRendererV2,
  flowStyles
} from "./chunk-X65FWQY7.js";
import {
  flowDb,
  parser$1
} from "./chunk-NYG6ALR3.js";
import "./chunk-AHX32WSI.js";
import "./chunk-FKD4JUCL.js";
import "./chunk-V5RA4XD2.js";
import "./chunk-R35T5PZF.js";
import "./chunk-KU7CSALG.js";
import "./chunk-X5RNMGW3.js";
import {
  require_dayjs_min,
  require_dist,
  setConfig
} from "./chunk-4JAZLTY5.js";
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
//# sourceMappingURL=flowDiagram-v2-58f49b84-VPS4QKUW.js.map
