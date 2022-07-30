// dropdown handler
let setCount = 0;

function toggleMenu() {
    let toggle = document.querySelector('.toggle');
    let navigation = document.querySelector('.navigation');
    let main = document.querySelector('.main');
    toggle.classList.toggle('active');
    navigation.classList.toggle('active');
    main.classList.toggle('active');

    document.getElementById('device').style.display="none";
    document.getElementById('user').style.display="none";
    document.getElementById('alert').style.display="none";
}

function closeNav(){
    if(window.innerWidth <= 726 & setCount!=1){        
        toggleMenu();
    }
    setCount = 0;
}

document.getElementById("navigation").addEventListener("click", closeNav);


/************  Dropdown Functions  ***********/

function setclickDropdown(){
 setCount = 1;
}

function showDropdown(ids){
    let navWidth = document.getElementById('navigation').offsetWidth;

    if(document.getElementById(ids).style.display != 'none'){
        document.getElementById(ids).style.display="none";
    }else if(navWidth > 70){
        document.getElementById(ids).style.display="unset";
    }
    
}