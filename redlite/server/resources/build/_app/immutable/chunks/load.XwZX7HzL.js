import{r as H,i as b,E as ee,h as oe,j as g,l as X,k as N,m as P,n as ue,o as z,q as fe,v as ie,w as ve,x as U,y as he,z as _e,A as pe,f as Q}from"./runtime.WC_eNKni.js";import{z as we,A as L,B as ne,S as Z,C as le,D as x,E as re,F as ae,G as Ee,H as y,I as F,J as Ae}from"./render.YmZxp1qF.js";const J=-1,G=99999999,te=-2;function de(){}function se(e,c,n,r,s,u,_){const E=(n&z)!==0,a=fe(n,e);let p=null;we(e,E);let C,h=null,f=null;a.r=l=>{const i=p,t=i.s;t.add(l),l.f(()=>{t.delete(l),t.size===0&&i.e!==null&&(i.d!==null&&(L(i.d),i.d=null),g(i.e),i.e=null)})};const v=()=>{const l={d:null,e:null,s:new Set,p},i=H(()=>{const t=a.d;t!==null&&(L(t),a.d=null);let w=a.a;(a.f&z)!==0&&(w=Ae(),a.a.appendChild(w)),u(w),l.d=a.d,a.d=null},a,!0);l.e=i,p=l},o=l=>{const i=l.f,t=(i&z)!==0,w=l.a;_(C,l,w,t,s,i,!0,h)},A=H(()=>{const l=c();C=b(l)?l:l==null?[]:Array.from(l),r!==null?h=C.map(r):n&ee||C.map(de);const i=C.length;if(u!==null){if(i===0){if(a.v.length!==0||f===null){o(a),v();return}}else if(a.v.length===0&&p!==null){const t=p,w=t.s;w.size===0?t.d!==null&&(L(t.d),t.d=null):ne(w,"out")}}f!==null&&ie(f)},a,!1);f=H(o,a,!0),oe(A,()=>{const l=a.f,i=a.a,t=(l&z)!==0;let w=p;for(;w!==null;){const I=w.d;I!==null&&L(I);const D=w.e;D!==null&&g(D),w=w.p}_([],a,i,t,s,l,!1,h),g(f)}),a.e=A}function Oe(e,c,n,r,s,u){se(e,c,n,r,s,u,Ie)}function Le(e,c,n,r,s){se(e,c,n,null,r,s,Ce)}function Ce(e,c,n,r,s,u,_){var E=Z in e&&e[Z].i,a=c.v,p=c.s;E&&(u&=~N);var C=a.length,h=e.length,f=Math.max(C,h),v=0,o,A;if(p.length!==0&&ce(p),h===0)for(o=[],r&&C!==0&&le(n);v<f;)A=a[v++],$(A,p,_,r);else{var l;if(o=Array(h),x!==null)for(var i=x[0];v<f;v++){l=E?X(e,v):e[v];var t=re(i);ae(t),i=t.at(-1).nextSibling.nextSibling,A=S(l,null,v,s,u),o[v]=A}else for(;v<f;v++)v>=C?(l=E?X(e,v):e[v],A=S(l,null,v,s,u),o[v]=A,B(A,n,r,null)):v>=h?(A=a[v],$(A,p,_)):(l=e[v],A=a[v],o[v]=A,T(A,l,v,u))}c.v=o}function Ie(e,c,n,r,s,u,_,E){var a=c.v;const p=E!==null;var C=c.s,h=a.length,f=e.length,v,o;if(C.length!==0&&ce(C),f===0)for(v=[],r&&h!==0&&le(n);h>0;)o=a[--h],$(o,C,_,r);else{var A=h-1,l=f-1,i,t,w;if(v=Array(f),x!==null)for(var I,D=x[0];f>0;)w=l- --f,t=e[w],i=p?E[w]:t,I=re(D),ae(I),D=(I.at(-1)||D).nextSibling.nextSibling,o=S(t,i,w,s,u),v[w]=o;else if(h===0)for(;f>0;)w=l- --f,t=e[w],i=p?E[w]:t,o=S(t,i,w,s,u),v[w]=o,B(o,n,r,null);else{var K=(u&ve)!==0,R=(u&(N|U))!==0||K,d=0,M=null;t=e[l],i=p?E[l]:t;e:for(;;){for(;a[A].k===i;){if(o=a[A--],t=e[l],R&&T(o,t,l,u),M=k(o),v[l]=o,d>--l||d>A)break e;i=p?E[l]:t}for(t=e[d],i=p?E[d]:t;d<=A&&d<=l&&a[d].k===i;)t=e[d],o=a[d],R&&T(o,t,d,u),v[d]=o,++d,i=p?E[d]:e[d];break}if(d>A)for(;l>=d;)t=e[l],i=p?E[l]:t,o=S(t,i,l,s,u),v[l--]=o,M=B(o,n,r,M);else if(d>l){f=d;do(o=a[f++])!==null&&$(o,C,_);while(f<=A)}else{var j=0,O=l-d+1,m=new Int32Array(O),V=new Map;for(f=0;f<O;++f)h=f+d,m[f]=J,t=e[h],i=p?E[h]:t,Ee(V,i,h);if(K)for(f=d;f<=A;++f)h=y(V,a[f].k),h!==void 0&&(t=e[h],o=a[f],T(o,t,h,u));for(f=d;f<=A;++f)h=y(V,a[f].k),o=a[f],h!==void 0?(j=j<h?h:G,m[h-d]=f,v[h]=o):o!==null&&$(o,C,_);j===G&&De(m);for(var Y,W,q;O-- >0;)l=O+d,h=m[O],q=h===-1,t=e[l],q?(i=p?E[l]:t,o=S(t,i,l,s,u)):(o=v[l],!K&&R&&T(o,t,l,u)),(q||j===G&&h!==te)&&(W=Y===void 0?M:k(Y),M=B(o,n,r,W)),v[l]=o,Y=o}}}c.v=v}function De(e){for(var c=e.length,n=new Int32Array(c),r=new Int32Array(c),s=0,u=0,_,E,a,p;e[u]===J;++u);for(r[0]=u++;u<c;++u)if(E=e[u],E!==J)if(_=r[s],e[_]<E)n[u]=_,r[++s]=u;else{for(a=0,p=s;a<p;)_=a+p>>1,e[r[_]]<E?a=_+1:p=_;E<e[r[a]]&&(a>0&&(n[u]=r[a-1]),r[a]=u)}for(_=r[s];s-->=0;)e[_]=te,_=n[_]}function B(e,c,n,r){var s=e.d;return r===null?n?F(s,c,null):F(s,c.parentNode,c):F(s,null,r)}function k(e){var c=e.d;return b(c)?c[0]:c}function ce(e){var c=e.length;if(c>0){for(var n=0,r,s;n<c;n++)r=e[n],s=r.r,s!==null&&(r.r=null,$(r,null,!1));e.length=0}}function T(e,c,n,r){r&N?P(e.v,c):ue(e.v)&&(e.v.o[e.v.p]=c);const s=e.s,u=(r&U)!==0,_=e.a;s!==null&&r&ee&&_!==null&&_(e,s),u?P(e.i,n):e.i=n}function $(e,c,n,r=!1){const s=e.s;if(n&&s!==null){for(let _ of s)_.r==="key"&&s.delete(_);if(s.size===0)e.s=null;else{ne(s,"out"),c!==null&&c.push(e);return}}const u=e.d;!r&&u!==null&&L(u),g(e.e)}function S(e,c,n,r,s){const _=(s&N)===0?e:s&_e?Q(e):pe(e),E=s&U?Q(n):n,a=he(_,E,c),p=H(C=>{r(null,C.v,C.i)},a,!0);return a.e=p,a}async function Te(e){return await(await fetch(`/api/runs/${e}/meta`)).json()}async function je(e){return await(await fetch(`/api/runs/${e}/data`)).json()}async function Se(){return await(await fetch("/api/runs")).json()}async function me(){const e={};for(const n of await Se()){const r=n.data_digest;e[`${r} ${n.metric} ${n.model}`]===void 0&&(e[`${r} ${n.metric} ${n.model}`]={data_digest:r,dataset:n.dataset,metric:n.metric,model:n.model,runs:[]}),e[`${r} ${n.metric} ${n.model}`].runs.push(n)}for(const n of Object.values(e))n.runs.sort((r,s)=>new Date(s.completed)-new Date(r.completed)),n.completed=n.runs[0].completed,n.score_summary=n.runs[0].score_summary;const c=[...Object.values(e)];return c.sort((n,r)=>new Date(r.completed)-new Date(n.completed)),c}export{Le as a,Te as b,je as c,me as d,Oe as e,Se as l};
