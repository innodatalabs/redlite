import"./disclose-version.bJ1TNjgf.js";import{a as h,p as b}from"./runtime.0RJBM7q3.js";import{f as w,g as y,d as g}from"./render.nzFa6Bvq.js";import{d as k,w as p}from"./entry.x9Y7B9uX.js";import{c as v}from"./load.VxHqMdKr.js";var D=g('<div class="text-center text-2xl mt-2"><p class="my-4">No data found.</p> <p>Did you create any runs?</p> <p>Did you set REDLITE_DATA_DIR environment correctly?</p> <p class="my-4">See <a class="text-blue-800" href="https://innodatalabs.github.io/redlite/">https://innodatalabs.github.io/redlite/</a> for the documentation.</p></div>');function N(o,r){h(r,!1);var s=y(o,!0,D);w(o,s),b()}const i=p(!1),_=(()=>{const{subscribe:o,set:r}=p([]);async function s(){try{i.set(!0);const n=await v();n.sort((m,l)=>new Date(l.completed)-new Date(m.completed)),r(n)}finally{i.set(!1)}}return s(),{subscribe:o,refresh:s}})(),d=o=>`${o.dataset} ${o.split} ${o.data_digest} ${o.metric}`,u=1e-4,S=k(_,(o,r)=>{const s={},n={};for(const e of o)s[e.model]===void 0&&(s[e.model]={model:e.model,tasks:{},winRate:0}),s[e.model].tasks[d(e)]===void 0&&(s[e.model].tasks[d(e)]={data_digest:e.data_digest,dataset:e.dataset,split:e.split,metric:e.metric,winner:!1,runs:[]}),s[e.model].tasks[d(e)].runs.push(e),n[d(e)]===void 0&&(n[d(e)]={taskHash:d(e),data_digest:e.data_digest,dataset:e.dataset,split:e.split,metric:e.metric,models:{},highestScore:0}),n[d(e)].models[e.model]===void 0&&(n[d(e)].models[e.model]={model:e.model,runs:[],wins:0}),n[d(e)].models[e.model].runs.push(e);for(const e of Object.values(n)){for(const t of Object.values(e.models))t.runs.sort((c,f)=>new Date(f.completed)-new Date(c.completed)),t.completed=t.runs[0].completed,t.score_summary=t.runs[0].score_summary;const a=Math.max(...Object.values(e.models).map(t=>t.score_summary.mean));e.highestScore=a;for(const t of Object.values(e.models))Math.abs(t.score_summary.mean-a)<u&&a>u&&(t.wins+=1,s[t.model].winRate+=1,s[t.model].tasks[e.taskHash].winner=!0)}for(const e of Object.values(s)){for(const a of Object.values(e.tasks))a.runs.sort((t,c)=>new Date(c.completed)-new Date(t.completed)),a.completed=a.runs[0].completed,a.score_summary=a.runs[0].score_summary;e.winRate/=Object.keys(n).length}const m=[...Object.values(s)];m.sort((e,a)=>a.winRate-e.winRate);const l=[...Object.values(n)];l.sort((e,a)=>new Date(a.completed)-new Date(e.completed)),r({models:m,tasks:l})},{models:[],tasks:[]});export{N,S as a,i as l,_ as r};