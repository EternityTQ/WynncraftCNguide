import {
  flowRendererV2,
  flowStyles
} from "./chunk-BKGI2KGL.js";
import {
  flowDb,
  parser$1
} from "./chunk-IOHE2GSR.js";
import "./chunk-YEPINHOW.js";
import "./chunk-YG53IXFQ.js";
import "./chunk-DPLPM6RV.js";
import "./chunk-UBUWTPGO.js";
import "./chunk-7IA2GDT4.js";
import "./chunk-JWJGTTQI.js";
import {
  require_dayjs_min,
  require_dist,
  setConfig
} from "./chunk-APGKDZR2.js";
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
//# sourceMappingURL=flowDiagram-v2-58f49b84-C2OW2LUB.js.map
