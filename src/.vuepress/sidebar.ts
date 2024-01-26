import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/quests/": [
    {
      text: "目录",
      icon: "laptop-code",
      prefix: "",
      children: [
        {
          text: "level 1~10",
          icon: "book",
          prefix: "lvl1-10/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 11~20",
          icon: "book",
          prefix: "lvl11-20/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 21~30",
          icon: "book",
          prefix: "lvl21-30/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 31~40",
          icon: "book",
          prefix: "lvl31-40/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 41~50",
          icon: "book",
          prefix: "lvl41-50/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 51~60",
          icon: "book",
          prefix: "lvl51-60/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 61~70",
          icon: "book",
          prefix: "lvl61-70/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 71~80",
          icon: "book",
          prefix: "lvl71-80/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 81~90",
          icon: "book",
          prefix: "lvl81-90/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 91~100",
          icon: "book",
          prefix: "lvl91-100/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "level 101~110",
          icon: "book",
          prefix: "lvl101-110/",
          children:"structure",
          collapsible: true,
        },
        {
          text: "特殊/过时任务",
          icon: "book",
          prefix: "special/",
          children:"structure",
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
        children:"structure",
      },{
        text: "进阶系统",
        prefix: "advancesystem/",
        icon: "scroll",
        collapsible: true,
        children:"structure",
      },"class","developmentroute","npcs","dungeon","profession","lootrun",{
        text: "RAID",
        prefix: "raid/",
        icon: "skull",
        collapsible: true,
        children:["intro","notg","nol","tcc","tna"],
      },"grindspot","earnle","VIP","festival","wynntils","slang","qa","support"],
    },
],
"/newbie/": [
],
});
