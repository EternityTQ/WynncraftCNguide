import { defineClientConfig } from "vuepress/client";
import CC from "./components/CopyCoord.vue";
import NPC from "./components/NPC.vue";
import Copy from "./components/Copy.vue";
import mob from "./components/Mob.vue";
export default defineClientConfig({
  enhance: ({ app, router, siteData }) => {
    app.component("CC", CC);
    app.component("NPC", NPC);
    app.component("Copy", Copy);
    app.component("mob", mob);
  },
});