import"../chunks/disclose-version.bJ1TNjgf.js";import{u as x,B as y,r as w,p as c,a as v,s as k}from"../chunks/runtime.WC_eNKni.js";import{w as D,f as h,g as p,m as l,t as M,a as u,d as m,x as R,s as a}from"../chunks/render.X6cabRiE.js";import{p as j}from"../chunks/stores.A5y-499H.js";import{g as B}from"../chunks/entry.2VBDmEnV.js";var C=(d,e,o)=>e(o.path),S=m('<div class="mr-4 text-base font-medium text-gray-600 pt-2 pb-2 box-border border border-b-2 border-white" role="presentation"> </div>');function i(d,e){v(e,!0);const o={};x(o);const r=()=>k(j,"$page",o);let s=y(e,"hidden",3,!1);var t=p(d,!0,S),n=u(t);w(()=>{l(t,"hidden",s()&&r().route.id!==e.path),l(t,"cursor-pointer",!s()),l(t,"hover:text-gray-900",!s()&&r().route.id!==e.path),l(t,"hover:text-blue-700",!s()&&r().route.id===e.path),l(t,"border-b-blue-600",r().route.id===e.path),l(t,"text-blue-600",r().route.id===e.path),M(n,e.label)}),t.__click=[C,B,e],h(d,t),c()}D(["click"]);var q=m('<div class="parent font-system svelte-1plg26p"><header class="flex pl-2 flex-rows items-center content-center justify-start text-gray-500 box-border border-b border-b-gray-300 shadow"><!> <!> <!> <!> <!></header> <div class="overflow-auto"><!></div></div>');function H(d,e){v(e,!1);var o=p(d,!0,q),r=u(o),s=u(r),t=a(a(s)),n=a(a(t)),b=a(a(n)),f=a(a(b)),g=a(a(r)),_=u(g);R(_,e.children,{},null),i(s,{label:"Models",path:"/models"}),i(t,{label:"Datasets",path:"/datasets"}),i(n,{label:"Runs",path:"/run"}),i(b,{label:"Run Details",path:"/run/[name]",hidden:!0}),i(f,{label:"Compare Models",path:"/compare/[digest]/[metric]",hidden:!0}),h(d,o),c()}export{H as component};
