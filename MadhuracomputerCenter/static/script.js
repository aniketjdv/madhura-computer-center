learn_btn=document.getElementById("learn-btn")
learn_btn.addEventListener("click", learnfn);

function learnfn() {
    console.log("OK");
    window.location.href = "/about";
}


document.getElementById("klic_banner_indexpage").addEventListener("click",gotoklickpage)
function gotoklickpage(){
    window.location.href = "/klic_course";
}

document.getElementById("mscit_banner_indexpage").addEventListener("click",gotomscitpage)
function gotomscitpage(){
    window.location.href = "/mscit";
}