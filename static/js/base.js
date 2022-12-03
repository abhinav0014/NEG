const toggle = document.getElementById('toggledark');


if(localStorage.getItem('theme')==null){
localStorage.setItem('theme','light');
}
let localData = localStorage.getItem('theme');

if (localData=='light'){
    toggle.className = "fa-solid fa-moon";  
    document.body.classList.remove('dark-theme');
}else if (localData=='dark'){
    toggle.className = "fa-regular fa-sun";  
    document.body.classList.add('dark-theme');
}
toggle.addEventListener('click', function () {
    document.body.classList.toggle("dark-theme");
    if (document.body.classList.contains("dark-theme")) {
        toggle.className = "fa-regular fa-sun";
        localStorage.setItem('theme','dark');
    } else {
        toggle.className = "fa-solid fa-moon";
        localStorage.setItem('theme','light');
    }
});

console.log('hehheheheheheheh what are u doin!');


