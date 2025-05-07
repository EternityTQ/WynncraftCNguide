import { defineClientConfig } from "vuepress/client";
import CC from "./components/CopyCoord.vue";
import NPC from "./components/NPC.vue";
import Copy from "./components/Copy.vue";
import mob from "./components/Mob.vue";
import guard from "./components/Guard.vue";
import skill from "./components/Skill.vue";
import tip from "./components/Tip.vue"
import gt from "./components/GlitchText.vue"
export default defineClientConfig({
  enhance: ({ app, router, siteData }) => {
    app.component("CC", CC);
    app.component("NPC", NPC);
    app.component("Copy", Copy);
    app.component("mob", mob);
    app.component("guard", guard);
    app.component("skill", skill);
    app.component("tip", tip);
    app.component("gt", gt);
  },
});