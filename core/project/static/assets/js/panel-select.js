document.addEventListener("DOMContentLoaded", function () {
    // current URL
    const currentUrl = window.location.href;
    console.log(currentUrl);

    //tabs
    const sermonTab = document.getElementById("tab1");
    const bookTab2 = document.getElementById("tab2");
    const tab1Pane = document.getElementById("tab1-pane");
    const tab2Pane = document.getElementById("tab2-pane");

    
    // check if the URL contains "sermon" or "books"
    if  (currentUrl.includes("sermons") || currentUrl.includes("media_page") || currentUrl.includes("books")){
        // reset active class
        sermonTab.classList.remove("active");
        bookTab2.classList.remove("active");
        tab1Pane.classList.remove("active", "show");
        tab2Pane.classList.remove("active", "show");

        if (currentUrl.includes("sermons") || currentUrl.includes("media_page")) {
            // activate sermons-related tab
            sermonTab.classList.add("active");
            document.querySelector("#tab1").setAttribute("aria-selected", "true");
            document.querySelector("#tab2").setAttribute("aria-selected", "false");
            tab1Pane.classList.add("active", "show");
        } else if (currentUrl.includes("books")) {
            // activate the books tab
            bookTab2.classList.add("active");
            document.querySelector("#tab1").setAttribute("aria-selected", "false");
            document.querySelector("#tab2").setAttribute("aria-selected", "true");
            tab2Pane.classList.add("active", "show");
        }
    }
});
