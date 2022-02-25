const VIDEO = document.getElementById('video');
const offsetCloseBtnHidden = document.getElementById('hiddenBtn');
const offsetShowBtnHidden = document.getElementById('shownBtn');

// VIDEO.onloadeddata = function() {
//     console.log("Video loaded");
//     setTimeout(() => {
//         loadend();
//     }, 2000);
// };
document.onreadystatechange = function() {
    if (document.readyState !== "complete") {
        console.log("loaded");
        setTimeout(() => {
            loadend();
        }, 2000);
    } else {
        console.log("not loaded");
        setTimeout(() => {
            loadend();
        }, 2000);
    }
};

function closeAfterSometimePC() {
    document.getElementById('pcham').classList.toggle('active')
    setTimeout(() => {
        offsetCloseBtnHidden.click()
        document.getElementById('pcham').classList.toggle('active')
    }, 800);
}
function closeAfterSometimeMob(){
    document.getElementById('ocanva').classList.toggle('active')
    // setTimeout(() => {
        offsetShowBtnHidden.click()
        // }, 650);
}
function loadend() {
    document.getElementById('loading').style.display= "none";
    document.getElementById('root').style.display= "block";
}