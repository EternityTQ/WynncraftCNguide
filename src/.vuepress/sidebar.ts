import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/quests/": [
    {
      text: "目录",
      icon: "laptop-code",
      link: "",
      prefix: "",
      children: [
        {
          text: "level 1~10",
          icon: "book",
          prefix: "lvl1-10/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 11~20",
          icon: "book",
          prefix: "lvl11-20/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 21~30",
          icon: "book",
          prefix: "lvl21-30/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 31~40",
          icon: "book",
          prefix: "lvl31-40/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 41~50",
          icon: "book",
          prefix: "lvl41-50/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 51~60",
          icon: "book",
          prefix: "lvl51-60/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 61~70",
          icon: "book",
          prefix: "lvl61-70/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 71~80",
          icon: "book",
          prefix: "lvl71-80/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 81~90",
          icon: "book",
          prefix: "lvl81-90/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 91~100",
          icon: "book",
          prefix: "lvl91-100/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 101~110",
          icon: "book",
          prefix: "lvl101-110/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "特殊/过时任务",
          icon: "book",
          prefix: "special/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "值得做的任务",
          icon: "money-bill",
          link: "valued/valued_quest.md",
          collapsible: true,
        },
      ],
    },
  ],
  "/guide/": [
    {
      text: "目录",
      icon: "laptop-code",
      prefix: "",
      children: [{
        text: "基础系统",
        prefix: "basesystem/",
        icon: "scroll",
        collapsible: true,
        children: "structure",
      }, {
        text: "进阶系统",
        prefix: "advancesystem/",
        icon: "scroll",
        collapsible: true,
        children: "structure",
      },{
        text: "常用功能",
        prefix: "commonfunction/",
        icon: "gear",
        collapsible: true,
        children: "structure",
      }, "class", {
        text: "新手指南",
        link: "/newbie/",
        icon: "route",
        collapsible: true,
      }, "npcs", "dungeon", "profession", {
        text: "RAID",
        prefix: "raid/",
        icon: "skull",
        collapsible: true,
        children: ["intro","newbie", "notg", "nol", "tcc", "tna"],
      }, "grindspot", "earnle", "vip", "festival", "mod", "slang", "community", "qa", "support","rules","history","howtoupdate"],
    },
  ],
  "/newbie/": [
    {
      text: "目录",
      icon: "laptop-code",
      link: "README",
      prefix: "",
      children: [
        "beforegame",
        {
          text: "level 1~10",
          icon: "gamepad",
          prefix: "lvl1-10/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 11~20",
          icon: "gamepad",
          prefix: "lvl11-20/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 21~30",
          icon: "gamepad",
          prefix: "lvl21-30/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 31~40",
          icon: "gamepad",
          prefix: "lvl31-40/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 41~50",
          icon: "gamepad",
          prefix: "lvl41-50/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 51~60",
          icon: "gamepad",
          prefix: "lvl51-60/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 61~70",
          icon: "gamepad",
          prefix: "lvl61-70/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 71~80",
          icon: "gamepad",
          prefix: "lvl71-80/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 81~90",
          icon: "gamepad",
          prefix: "lvl81-90/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 91~100",
          icon: "gamepad",
          prefix: "lvl91-100/",
          children: "structure",
          collapsible: true,
        },
        {
          text: "level 101~110",
          icon: "gamepad",
          prefix: "lvl101-110/",
          children: "structure",
          collapsible: true,
        },
      ],
    },
  ],
});
