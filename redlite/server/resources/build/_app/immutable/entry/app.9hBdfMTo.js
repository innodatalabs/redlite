import{C as B,c as I,D as q,a as M,B as y,F as N,g as h,p as U,f as R,e as b,t as j}from"../chunks/runtime.g9XoCGco.js";import{M as F,i as P,N as k,c as g,m as W,e as T,b as p,s as x,a as z,o as G,g as L,f as H,q as J,d as V,p as K,l as w}from"../chunks/disclose-version.aiVGvucR.js";function Q(n){return class extends X{constructor(t){super({component:n,...t})}}}class X{#t={};#e;constructor(t){this.#e=F(t.component,{target:t.target,props:{...t.props,$$events:this.#t},context:t.context,intro:t.intro,recover:t.recover});for(const e of Object.keys(this.#e))e==="$set"||e==="$destroy"||B(this,e,{get(){return this.#e[e]},set(a){this.#e[e]=a},enumerable:!0})}$set(t){this.#e.$set(t)}$on(t,e){this.#t[t]=this.#t[t]||[];const a=(...i)=>e.call(this,...i);return this.#t[t].push(a),()=>{this.#t[t]=this.#t[t].filter(i=>i!==a)}}$destroy(){this.#e.$destroy()}}function Y(n){I(()=>{const t=q(n);if(typeof t=="function")return t})}const Z="modulepreload",$=function(n,t){return new URL(n,t).href},A={},_=function(t,e,a){let i=Promise.resolve();if(e&&e.length>0){const c=document.getElementsByTagName("link");i=Promise.all(e.map(r=>{if(r=$(r,a),r in A)return;A[r]=!0;const m=r.endsWith(".css"),v=m?'[rel="stylesheet"]':"";if(!!a)for(let s=c.length-1;s>=0;s--){const o=c[s];if(o.href===r&&(!m||o.rel==="stylesheet"))return}else if(document.querySelector(`link[href="${r}"]${v}`))return;const l=document.createElement("link");if(l.rel=m?"stylesheet":Z,m||(l.as="script",l.crossOrigin=""),l.href=r,document.head.appendChild(l),m)return new Promise((s,o)=>{l.addEventListener("load",s),l.addEventListener("error",()=>o(new Error(`Unable to preload CSS for ${r}`)))})}))}return i.then(()=>t()).catch(c=>{const r=new Event("vite:preloadError",{cancelable:!0});if(r.payload=c,window.dispatchEvent(r),!r.defaultPrevented)throw c})},at={};var tt=V('<div id="svelte-announcer" aria-live="assertive" aria-atomic="true" style="position: absolute; left: 0; top: 0; clip: rect(0 0 0 0); clip-path: inset(50%); overflow: hidden; white-space: nowrap; width: 1px; height: 1px"><!></div>'),et=V("<!> <!>",!0);function rt(n,t){M(t,!0);let e=y(t,"components",11,()=>[]),a=y(t,"data_0",3,null),i=y(t,"data_1",3,null);N(()=>t.stores.page.set(t.page)),I(()=>{t.stores,t.page,t.constructors,e(),t.form,a(),i(),t.stores.page.notify()});let c=R(!1),r=R(!1),m=R(null);Y(()=>{const s=t.stores.page.subscribe(()=>{h(c)&&(b(r,!0),j().then(()=>{b(m,K(document.title||"untitled page"))}))});return b(c,!0),s});var v=G(n,!0,et),E=p(v),l=x(x(E));P(E,()=>t.constructors[1],s=>{var o=L(s),d=p(o);k(d,()=>t.constructors[0],f=>{w(f(d,{get data(){return a()},children:(u,st)=>{var O=L(u),D=p(O);k(D,()=>t.constructors[1],C=>{w(C(D,{get data(){return i()},get form(){return t.form}}),S=>e()[1]=S)}),g(u,O)}}),u=>e()[0]=u)}),g(s,o)},s=>{var o=L(s),d=p(o);k(d,()=>t.constructors[0],f=>{w(f(d,{get data(){return a()},get form(){return t.form}}),u=>e()[0]=u)}),g(s,o)}),P(l,()=>h(c),s=>{var o=H(s,!0,tt),d=z(o);P(d,()=>h(r),f=>{var u=J(f);W(u,()=>h(m)),T(f,u)},null),T(s,o)},null),g(n,v),U()}const it=Q(rt),ct=[()=>_(()=>import("../nodes/0.X3MM7aF3.js"),__vite__mapDeps([0,1,2,3,4,5]),import.meta.url),()=>_(()=>import("../nodes/1.lZ4PIQDt.js"),__vite__mapDeps([6,1,2,3,4]),import.meta.url),()=>_(()=>import("../nodes/2.KrKFrezb.js"),__vite__mapDeps([7,1,2,8,4,9,10,11]),import.meta.url),()=>_(()=>import("../nodes/3.KT_BYWzH.js"),__vite__mapDeps([12,1,2,8,3,4,13,11,14,15]),import.meta.url),()=>_(()=>import("../nodes/4.P9VkWpZY.js"),__vite__mapDeps([16,1,2,8,4,11,13,17,9]),import.meta.url),()=>_(()=>import("../nodes/5.2rrsoyp5.js"),__vite__mapDeps([18,1,2,8,4,11,13,17,9]),import.meta.url),()=>_(()=>import("../nodes/6.-67jWeS9.js"),__vite__mapDeps([19,1,2,8,3,4,14,15,11,13]),import.meta.url),()=>_(()=>import("../nodes/7.fF5K6gpk.js"),__vite__mapDeps([20,1,2,10,11]),import.meta.url)],lt=[],ut={"/":[2],"/compare/[digest]/[metric]":[3],"/datasets":[4],"/models":[5],"/run/[name]":[6],"/test":[7]},mt={handleError:({error:n})=>{console.error(n)},reroute:()=>{}};export{ut as dictionary,mt as hooks,at as matchers,ct as nodes,it as root,lt as server_loads};
function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = ["../nodes/0.X3MM7aF3.js","../chunks/disclose-version.aiVGvucR.js","../chunks/runtime.g9XoCGco.js","../chunks/stores.kKdIAdUz.js","../chunks/entry.H1E4yJl7.js","../assets/0.YqvfxNAp.css","../nodes/1.lZ4PIQDt.js","../nodes/2.KrKFrezb.js","../chunks/load.U24AIlaj.js","../chunks/data.m4-QM_Am.js","../chunks/RunCard.UyCSDHCS.js","../chunks/util.xL8_OAi2.js","../nodes/3.KT_BYWzH.js","../chunks/Bubble.8QeVWBuV.js","../chunks/ExpandableTextBlock.YMPc9NeF.js","../assets/ExpandableTextBlock.Qzqq2fXU.css","../nodes/4.P9VkWpZY.js","../chunks/Model.oIPLRDiD.js","../nodes/5.2rrsoyp5.js","../nodes/6.-67jWeS9.js","../nodes/7.fF5K6gpk.js"]
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}
