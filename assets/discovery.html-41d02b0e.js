import{_ as o}from"./plugin-vue_export-helper-c27b6911.js";import{o as n,c as i,e,d as t}from"./app-5fe4699b.js";const s={},c=e("p",null,[t("this.tooltipTop = event.pageY + 10; // 根据需要调整偏移量"),e("br"),t(" this.tooltipLeft = event.pageX + 10; // 根据需要调整偏移量")],-1),l=e("pre",null,[e("code",null,`   if (event.clientX > window.innerWidth / 2 && this.$refs.tooltip) {
    this.tooltipLeft = event.pageX-this.$refs.tooltip.clientWidth - 100; // 20为调整的偏移量
  }
`)],-1),r=[c,l];function _(a,d){return n(),i("div",null,r)}const h=o(s,[["render",_],["__file","discovery.html.vue"]]);export{h as default};
