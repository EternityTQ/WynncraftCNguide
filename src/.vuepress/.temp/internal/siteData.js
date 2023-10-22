export const siteData = JSON.parse("{\"base\":\"/WynncraftCNguide/\",\"lang\":\"zh-CN\",\"title\":\"Wynncraft中文攻略\",\"description\":\"Wynncraft中文攻略\",\"head\":[[\"link\",{\"rel\":\"preconnect\",\"href\":\"https://fonts.googleapis.com\"}],[\"link\",{\"rel\":\"preconnect\",\"href\":\"https://fonts.gstatic.com\",\"crossorigin\":\"\"}],[\"link\",{\"href\":\"https://fonts.googleapis.com/css2?family=Montserrat:wght@500&family=Noto+Sans+SC&display=swap\",\"rel\":\"stylesheet\"}],[\"link\",{\"rel\":\"icon\",\"href\":\"/WynncraftCNguide/favicon.ico\"}]],\"locales\":{}}")

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
