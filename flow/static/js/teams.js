var category=0

colorPalette=["#0a043c","#03506f","#4cd3c2","#b7efcd"]

teams=JSON.parse(document.getElementById("teams").textContent)
members=JSON.parse(document.getElementById("members").textContent)
console.log(teams)
console.log(members)


var no_of_categories=teams.length;

var left=document.getElementsByClassName('fa-backward')[0]
var right=document.getElementsByClassName('fa-forward')[0]

const changeTeams=()=>{
    var no_of_cards=members[category].length;

    console.log(category,"category")
    console.log("changing category",teams[category].name,no_of_cards,members[category][0])

    document.getElementById("cards").innerHTML="";

    for(let i=1;i<=no_of_cards;i++)
    {
        document.getElementById("cards").innerHTML+=
        `<div class="card glitch" id="card${i}" card_no="${i}">
            <img src="static/aarhnLogo.png" alt="">
            <div class="glitch__layers">
                <div class="glitch__layer"></div>
                <div class="glitch__layer"></div>
                <div class="glitch__layer"></div>
            </div>
            <h1 class="member-details name">Name</h1>
            <h3 class="member-details name">Club Name</h3>
        </div>`
    }

    for(let j=0;j<no_of_cards;j++)
    {
        const image=`media\/${members[category][j].profile_img}`
        document.querySelector(`#card${j+1} img`).src=image;
        document.querySelectorAll(`#card${j+1} div.glitch__layers div.glitch__layer`).forEach((layer)=>layer.style.backgroundImage=`url(${image})`)
    }

    const cards=document.querySelectorAll(".card img")

    document.querySelectorAll(".card").forEach((card)=>{
        let memberDetails=document.getElementById("member-details")
        let teamCategory=document.getElementById("team-category")
        
        card.addEventListener("mouseover",()=>{
            card.classList.add("sparkle")
            card.style.zIndex=2

            let memberName=document.getElementById("member-name")
            let memberClub=document.getElementById("member-club")
            let memberPosition=document.getElementById("member-position")

            console.log(category,"cat now")

            let card_no=card.getAttribute("card_no")
            if(category==0)
            cat=no_of_categories-1
            else
            cat=category-1
            console.log("card no", members[cat][card_no-1].name)
            let name= `${members[cat][card_no-1].name}`
            let club= `${members[cat][card_no-1].choice}`
            let position= `${members[cat][card_no-1].position}`

            memberName.innerHTML=name
            memberClub.innerHTML=club
            memberPosition.innerHTML=position

            memberName.setAttribute("data-text",name)
            memberPosition.setAttribute("data-text",position)
            memberClub.setAttribute("data-text",club)

            memberDetails.style.display="flex"
            teamCategory.style.display="none"
        })
        card.addEventListener("mouseleave",()=>{
            card.classList.remove("sparkle")
            card.style.zIndex=0;

            memberDetails.style.display="none"
            teamCategory.style.display="flex"
        })
    })
        
    let teamCategory=`${teams[category].name}`
    let categoryTag=document.getElementById("team-category")
    categoryTag.innerHTML=teamCategory

    document.getElementById("team-category").setAttribute("data-text",teamCategory)
    
    document.getElementById("color-css").href=`../static/css/teams/teams${category%3+1}.css`
}

left.addEventListener("click", ()=>{
    category--;
    if(category<0)
    category=no_of_categories-1
    changeTeams()
})

right.addEventListener("click", ()=>{
    category++;
    if(category==no_of_categories)
    category=0
    changeTeams()
})


const changeColor=()=>{
    changeTeams()

    category++;
    if(category==no_of_categories)
        category=0

    setTimeout(()=>{
        changeColor()
    },20000)
}

changeColor()
