export const siteData = JSON.parse("{\"base\":\"/WynncraftCNguide/\",\"lang\":\"zh-CN\",\"title\":\"Wynncraft中文攻略\",\"description\":\"Wynncraft中文攻略\",\"head\":[[\"link\",{\"rel\":\"icon\",\"href\":\"/WynncraftCNguide/favicon.ico\"}]],\"locales\":{}}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateSiteData) {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ siteData }) => {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  })
}
