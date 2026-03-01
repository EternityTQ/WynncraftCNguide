import { defineClientConfig } from "vuepress/client";
import CC from "./components/CopyCoord.vue";
import NPC from "./components/NPC.vue";
import Copy from "./components/Copy.vue";
import mob from "./components/Mob.vue";
import guard from "./components/Guard.vue";
import skill from "./components/Skill.vue";
import tip from "./components/Tip.vue"
import SkillNode from "./components/SkillNode.vue"
import SkillTree from "./components/SkillTree.vue";
import gt from "./components/GlitchText.vue"
import jc from "./components/JobCard.vue"
import ks from "./components/KeySkills.vue"
import pc from "./components/ProfessionCard.vue"
import rb from "./components/rb.vue"
import MythicItem from "./components/MythicItem.vue"
import ipb from "./components/ItemPanelBlock.vue"
export default defineClientConfig({
  enhance: ({ app, router, siteData }) => {
    app.component("CC", CC);
    app.component("NPC", NPC);
    app.component("Copy", Copy);
    app.component("mob", mob);
    app.component("guard", guard);
    app.component("skill", skill);
    app.component("tip", tip);
    app.component("sn", SkillNode);
    app.component("st", SkillTree);
    app.component("gt", gt);
    app.component("jc", jc);
    app.component("ks", ks);
    app.component("pc", pc);
    app.component("rb",rb);
    app.component("MythicItem", MythicItem);
    app.component("ipb",ipb);

  },
});