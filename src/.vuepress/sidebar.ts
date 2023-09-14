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
      ],
    },
  ],
  "/guide/": [
    {
      text: "目录",
      icon: "laptop-code",
      prefix: "",
      children: "structure",
    },
],
});
