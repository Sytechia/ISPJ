var alanBtnInstance = alanBtn({
    key: "a763dd391abe149ad60c63f9a0944d002e956eca572e1d8b807a3e2338fdd0dc/stage",
    onCommand: function (commandData) {
    if (commandData.command === "open-cart"){
        document.querySelector('.cd-img-replace').click()
    }
    else if (commandData.command === "check-out"){
        setTimeout(()=> window.location.href = '/checkout', 2000)
    }
    else if (commandData.command === "clear-cart"){
        $.ajax({
            type: "GET",
            url: `/shop?removeAll=true`
        })
        setTimeout(()=> window.location.reload(), 2000)
    }

    // Adding Games //

    // Hades game 
    else if (commandData.command === "Hades"){
        let game = "Hades"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText('Hades has alreay been added to your cart! Please add something else')
        } else {
            $.ajax({
                type: "GET",
                url: `/shop?id=1`
            })
            alanBtnInstance.playText('Hades has been added to your cart')
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Cyber Punk 2077
    else if (commandData.command === "Cyber Punk 2077"){
        let game = "Cyber Punk 2077"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText('Cyber Punk 2077 has alreay been added to your cart! Please add something else')
        } else {
            $.ajax({
                type: "GET",
                url: `/shop?id=3`
            })
            alanBtnInstance.playText('Cyber Punk 2077 has been added to your cart')
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Rocket League
    else if (commandData.command === "Rocket League"){
        let game = "Cyber Punk 2077"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText('Rocket League has alreay been added to your cart! Please add something else')
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=4"
            })
            alanBtnInstance.playText('Rocket League has been added to your cart')
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Rocket League
    else if (commandData.command === "Rocket League"){
        let game = "Rocket League"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Rocket League has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=4"
            })
            alanBtnInstance.playText("Rocket League has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // GTA V 
    else if (commandData.command === "gtaV"){
        let game = "GTA V"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText('gta 5 has alreay been added to your cart! Please add something else')
        } else {
            $.ajax({
                type: "GET",
                url: `/shop?id=5`
            })
            alanBtnInstance.playText('gta 5 has been added to your cart')
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Parkasaurus
    else if (commandData.command === "Parkasaurus"){
        let game = "Parkasaurus"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Parkasaurus has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=6"
            })
            alanBtnInstance.playText("Parkasaurus has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Minion Masters
    else if (commandData.command === "Minion Masters"){
        let game = "Minion Masters"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Minion Masters has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=7"
            })
            alanBtnInstance.playText("Minion Masters has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Tom Clancy's Rainbow Six Siege
    else if (commandData.command === "Tom Clancy's Rainbow Six Siege"){
        let game = "Tom Clancy's Rainbow Six Siege"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Tom Clancy's Rainbow Six Siege has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=8"
            })
            alanBtnInstance.playText("Tom Clancy's Rainbow Six Siege has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Terraria
    else if (commandData.command === "Terraria"){
        let game = "Terraria"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Terraria has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=9"
            })
            alanBtnInstance.playText("Terraria has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Dead by Daylight
    else if (commandData.command === "Dead by Daylight"){
        let game = "Dead by Daylight"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Dead by Daylight has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=10"
            })
            alanBtnInstance.playText("Dead by Daylight has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    } 
    // The Elder Scrolls V: Skyrim
    else if (commandData.command === "The Elder Scrolls V: Skyrim"){
        let game = "The Elder Scrolls V: Skyrim"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("The Elder Scrolls V: Skyrim has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=12"
            })
            alanBtnInstance.playText("The Elder Scrolls V: Skyrim has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    } 
    // Final Fantasy VII Remake
    else if (commandData.command === "Final Fantasy VII Remake"){
        let game = "Final Fantasy VII Remake"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Final Fantasy VII Remake has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=13"
            })
            alanBtnInstance.playText("Final Fantasy VII Remake has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    } 
    // Minecraft
    else if (commandData.command === "Minecraft"){
        let game = "Minecraft"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Minecraft has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=14"
            })
            alanBtnInstance.playText("Minecraft has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Uncharted 4: A Thief's End
    else if (commandData.command === "Uncharted 4: A Thief's End"){
        let game = "Uncharted 4: A Thief's End"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Uncharted 4: A Thief's End has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=15"
            })
            alanBtnInstance.playText("Uncharted 4: A Thief's End has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Assassin's Creed Odyssey
    else if (commandData.command === "Assassin's Creed Odyssey"){
        let game = "Assassin's Creed Odyssey"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Assassin's Creed Odyssey has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=16"
            })
            alanBtnInstance.playText("Assassin's Creed Odyssey has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Resident Evil 3
    else if (commandData.command === "Resident Evil 3"){
        let game = "Resident Evil 3"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Resident Evil 3 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=17"
            })
            alanBtnInstance.playText("Resident Evil 3 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // The Last of Us Part II
    else if (commandData.command === "The Last of Us Part II"){
        let game = "The Last of Us Part II"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("The Last of Us Part II has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=18"
            })
            alanBtnInstance.playText("The Last of Us Part II has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Stardew Valley
    else if (commandData.command === "Stardew Valley"){
        let game = "Stardew Valley"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Stardew Valley has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=19"
            })
            alanBtnInstance.playText("Stardew Valley has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Overcooked 2
    else if (commandData.command === "Overcooked 2"){
        let game = "Overcooked 2"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Overcooked 2 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=20"
            })
            alanBtnInstance.playText("Overcooked 2 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Fall Guys: Ultimate Knockout 
    else if (commandData.command === "Fall Guys: Ultimate Knockout "){
        let game = "Fall Guys: Ultimate Knockout "
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Fall Guys: Ultimate Knockout  has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=21"
            })
            alanBtnInstance.playText("Fall Guys: Ultimate Knockout  has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    } 
    // Forza Horizon 4 
    else if (commandData.command === "Forza Horizon 4 "){
        let game = "Forza Horizon 4 "
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Forza Horizon 4  has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=22"
            })
            alanBtnInstance.playText("Forza Horizon 4  has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Dirt 4
    else if (commandData.command === "Dirt 4"){
        let game = "Dirt 4"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Dirt 4 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=23"
            })
            alanBtnInstance.playText("Dirt 4 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // The Witcher 3: Wild Hunt
    else if (commandData.command === "The Witcher 3: Wild Hunt"){
        let game = "The Witcher 3: Wild Hunt"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("The Witcher 3: Wild Hunt has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=24"
            })
            alanBtnInstance.playText("The Witcher 3: Wild Hunt has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    } 
    // Persona 5 Strikers
    else if (commandData.command === "Persona 5 Strikers"){
        let game = "Persona 5 Strikers"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Persona 5 Strikers has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=25"
            })
            alanBtnInstance.playText("Persona 5 Strikers has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // The Legend of Zelda: Breath of the Wild
    else if (commandData.command === "The Legend of Zelda: Breath of the Wild"){
        let game = "The Legend of Zelda: Breath of the Wild"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("The Legend of Zelda: Breath of the Wild has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=26"
            })
            alanBtnInstance.playText("The Legend of Zelda: Breath of the Wild has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // The Sims 4
    else if (commandData.command === "The Sims 4"){
        let game = "The Sims 4"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("The Sims 4 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=27"
            })
            alanBtnInstance.playText("The Sims 4 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // WWE 2K Battlegrounds
    else if (commandData.command === "WWE 2K Battlegrounds"){
        let game = "WWE 2K Battlegrounds"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("WWE 2K Battlegrounds has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=28"
            })
            alanBtnInstance.playText("WWE 2K Battlegrounds has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // NBA 2K20
    else if (commandData.command === "NBA 2K20"){
        let game = "NBA 2K20"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("NBA 2K20 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=29"
            })
            alanBtnInstance.playText("NBA 2K20 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // FIFA 21
    else if (commandData.command === "FIFA 21"){
        let game = "FIFA 21"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("FIFA 21 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=30"
            })
            alanBtnInstance.playText("FIFA 21 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    } 
    // Animal Crossing: New Horizons
    else if (commandData.command === "Animal Crossing: New Horizons"){
        let game = "Animal Crossing: New Horizons"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Animal Crossing: New Horizons has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=31"
            })
            alanBtnInstance.playText("Animal Crossing: New Horizons has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Call of Duty: Black Ops Cold War
    else if (commandData.command === "Call of Duty: Black Ops Cold War"){
        let game = "Call of Duty: Black Ops Cold War"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Call of Duty: Black Ops Cold War has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=32"
            })
            alanBtnInstance.playText("Call of Duty: Black Ops Cold War has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // PlayerUnknown's Battlegrounds
    else if (commandData.command === "PlayerUnknown's Battlegrounds"){
        let game = "PlayerUnknown's Battlegrounds"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("PlayerUnknown's Battlegrounds has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=33"
            })
            alanBtnInstance.playText("PlayerUnknown's Battlegrounds has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Mario Kart 8
    else if (commandData.command === "Mario Kart 8"){
        let game = "Mario Kart 8"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Mario Kart 8 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=34"
            })
            alanBtnInstance.playText("Mario Kart 8 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Far Cry 5
    else if (commandData.command === "Far Cry 5"){
        let game = "Far Cry 5"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Far Cry 5 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=35"
            })
            alanBtnInstance.playText("Far Cry 5 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Star Wars Jedi: Fallen Order
    else if (commandData.command === "Star Wars Jedi: Fallen Order"){
        let game = "Star Wars Jedi: Fallen Order"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Star Wars Jedi: Fallen Order has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=36"
            })
            alanBtnInstance.playText("Star Wars Jedi: Fallen Order has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Watch Dogs 2
    else if (commandData.command === "Watch Dogs 2"){
        let game = "Watch Dogs 2"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Watch Dogs 2 has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=37"
            })
            alanBtnInstance.playText("Watch Dogs 2 has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    // Phasmophobia
    else if (commandData.command === "Phasmophobia"){
        let game = "Phasmophobia"
        let addornot = true        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                addornot = false
            }
        })
        if(addornot == false){
            alanBtnInstance.playText("Phasmophobia has alreay been added to your cart! Please add something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?id=38"
            })
            alanBtnInstance.playText("Phasmophobia has been added to your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }

    // Deleting Games //
    // Hades
    else if (commandData.command === "delete Hades"){
        let game = "Hades"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Hades is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Hades"
            })
            alanBtnInstance.playText("Hades has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Cyberpunk 2077
    else if (commandData.command === "delete Cyberpunk 2077"){
        let game = "Cyberpunk 2077"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Cyberpunk 2077 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Cyberpunk 2077"
            })
            alanBtnInstance.playText("Cyberpunk 2077 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Rocket League
    else if (commandData.command === "delete Rocket League"){
        let game = "Rocket League"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Rocket League is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Rocket League"
            })
            alanBtnInstance.playText("Rocket League has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // GTA V
    else if (commandData.command === "delete GTA V"){
        let game = "GTA V"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("GTA V is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=GTA V"
            })
            alanBtnInstance.playText("GTA V has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Parkasaurus
    else if (commandData.command === "delete Parkasaurus"){
        let game = "Parkasaurus"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Parkasaurus is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Parkasaurus"
            })
            alanBtnInstance.playText("Parkasaurus has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Minion Masters
    else if (commandData.command === "delete Minion Masters"){
        let game = "Minion Masters"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Minion Masters is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Minion Masters"
            })
            alanBtnInstance.playText("Minion Masters has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
 
    // Tom Clancy's Rainbow Six Siege
    else if (commandData.command === "delete Tom Clancy's Rainbow Six Siege"){
        let game = "Tom Clancy's Rainbow Six Siege"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Tom Clancy's Rainbow Six Siege is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Tom Clancy's Rainbow Six Siege"
            })
            alanBtnInstance.playText("Tom Clancy's Rainbow Six Siege has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
     
    // Terraria
    else if (commandData.command === "delete Terraria"){
        let game = "Terraria"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Terraria is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Terraria"
            })
            alanBtnInstance.playText("Terraria has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Dead by Daylight
    else if (commandData.command === "delete Dead by Daylight"){
        let game = "Dead by Daylight"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Dead by Daylight is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Dead by Daylight"
            })
            alanBtnInstance.playText("Dead by Daylight has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // The Elder Scrolls V: Skyrim
    else if (commandData.command === "delete The Elder Scrolls V: Skyrim"){
        let game = "The Elder Scrolls V: Skyrim"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("The Elder Scrolls V: Skyrim is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=The Elder Scrolls V: Skyrim"
            })
            alanBtnInstance.playText("The Elder Scrolls V: Skyrim has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
     
    // Final Fantasy VII Remake
    else if (commandData.command === "delete Final Fantasy VII Remake"){
        let game = "Final Fantasy VII Remake"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Final Fantasy VII Remake is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Final Fantasy VII Remake"
            })
            alanBtnInstance.playText("Final Fantasy VII Remake has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Minecraft
    else if (commandData.command === "delete Minecraft"){
        let game = "Minecraft"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Minecraft is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Minecraft"
            })
            alanBtnInstance.playText("Minecraft has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Uncharted 4: A Thief's End
    else if (commandData.command === "delete Uncharted 4: A Thief's End"){
        let game = "Uncharted 4: A Thief's End"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Uncharted 4: A Thief's End is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Uncharted 4: A Thief's End"
            })
            alanBtnInstance.playText("Uncharted 4: A Thief's End has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Assassin's Creed Odyssey
    else if (commandData.command === "delete Assassin's Creed Odyssey"){
        let game = "Assassin's Creed Odyssey"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Assassin's Creed Odyssey is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Assassin's Creed Odyssey"
            })
            alanBtnInstance.playText("Assassin's Creed Odyssey has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Resident Evil 3
    else if (commandData.command === "delete Resident Evil 3"){
        let game = "Resident Evil 3"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Resident Evil 3 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Resident Evil 3"
            })
            alanBtnInstance.playText("Resident Evil 3 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // The Last of Us Part II
    else if (commandData.command === "delete The Last of Us Part II"){
        let game = "The Last of Us Part II"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("The Last of Us Part II is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=The Last of Us Part II"
            })
            alanBtnInstance.playText("The Last of Us Part II has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Stardew Valley
    else if (commandData.command === "delete Stardew Valley"){
        let game = "Stardew Valley"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Stardew Valley is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Stardew Valley"
            })
            alanBtnInstance.playText("Stardew Valley has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Overcooked 2
    else if (commandData.command === "delete Overcooked 2"){
        let game = "Overcooked 2"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Overcooked 2 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Overcooked 2"
            })
            alanBtnInstance.playText("Overcooked 2 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Fall Guys: Ultimate Knockout 
    else if (commandData.command === "delete Fall Guys: Ultimate Knockout "){
        let game = "Fall Guys: Ultimate Knockout "
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Fall Guys: Ultimate Knockout  is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Fall Guys: Ultimate Knockout "
            })
            alanBtnInstance.playText("Fall Guys: Ultimate Knockout  has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Forza Horizon 4 
    else if (commandData.command === "delete Forza Horizon 4 "){
        let game = "Forza Horizon 4 "
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Forza Horizon 4  is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Forza Horizon 4 "
            })
            alanBtnInstance.playText("Forza Horizon 4  has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Dirt 4
    else if (commandData.command === "delete Dirt 4"){
        let game = "Dirt 4"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Dirt 4 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Dirt 4"
            })
            alanBtnInstance.playText("Dirt 4 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // The Witcher 3: Wild Hunt
    else if (commandData.command === "delete The Witcher 3: Wild Hunt"){
        let game = "The Witcher 3: Wild Hunt"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("The Witcher 3: Wild Hunt is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=The Witcher 3: Wild Hunt"
            })
            alanBtnInstance.playText("The Witcher 3: Wild Hunt has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Persona 5 Strikers
    else if (commandData.command === "delete Persona 5 Strikers"){
        let game = "Persona 5 Strikers"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Persona 5 Strikers is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Persona 5 Strikers"
            })
            alanBtnInstance.playText("Persona 5 Strikers has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // The Legend of Zelda: Breath of the Wild
    else if (commandData.command === "delete The Legend of Zelda: Breath of the Wild"){
        let game = "The Legend of Zelda: Breath of the Wild"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("The Legend of Zelda: Breath of the Wild is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=The Legend of Zelda: Breath of the Wild"
            })
            alanBtnInstance.playText("The Legend of Zelda: Breath of the Wild has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // The Sims 4
    else if (commandData.command === "delete The Sims 4"){
        let game = "The Sims 4"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("The Sims 4 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=The Sims 4"
            })
            alanBtnInstance.playText("The Sims 4 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // WWE 2K Battlegrounds
    else if (commandData.command === "delete WWE 2K Battlegrounds"){
        let game = "WWE 2K Battlegrounds"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("WWE 2K Battlegrounds is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=WWE 2K Battlegrounds"
            })
            alanBtnInstance.playText("WWE 2K Battlegrounds has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // NBA 2K20
    else if (commandData.command === "delete NBA 2K20"){
        let game = "NBA 2K20"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("NBA 2K20 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=NBA 2K20"
            })
            alanBtnInstance.playText("NBA 2K20 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // FIFA 21
    else if (commandData.command === "delete FIFA 21"){
        let game = "FIFA 21"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("FIFA 21 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=FIFA 21"
            })
            alanBtnInstance.playText("FIFA 21 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Animal Crossing: New Horizons
    else if (commandData.command === "delete Animal Crossing: New Horizons"){
        let game = "Animal Crossing: New Horizons"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Animal Crossing: New Horizons is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Animal Crossing: New Horizons"
            })
            alanBtnInstance.playText("Animal Crossing: New Horizons has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Call of Duty: Black Ops Cold War
    else if (commandData.command === "delete Call of Duty: Black Ops Cold War"){
        let game = "Call of Duty: Black Ops Cold War"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Call of Duty: Black Ops Cold War is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Call of Duty: Black Ops Cold War"
            })
            alanBtnInstance.playText("Call of Duty: Black Ops Cold War has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // PlayerUnknown's Battlegrounds
    else if (commandData.command === "delete PlayerUnknown's Battlegrounds"){
        let game = "PlayerUnknown's Battlegrounds"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("PlayerUnknown's Battlegrounds is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=PlayerUnknown's Battlegrounds"
            })
            alanBtnInstance.playText("PlayerUnknown's Battlegrounds has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Mario Kart 8
    else if (commandData.command === "delete Mario Kart 8"){
        let game = "Mario Kart 8"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Mario Kart 8 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Mario Kart 8"
            })
            alanBtnInstance.playText("Mario Kart 8 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Far Cry 5
    else if (commandData.command === "delete Far Cry 5"){
        let game = "Far Cry 5"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Far Cry 5 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Far Cry 5"
            })
            alanBtnInstance.playText("Far Cry 5 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Star Wars Jedi: Fallen Order
    else if (commandData.command === "delete Star Wars Jedi: Fallen Order"){
        let game = "Star Wars Jedi: Fallen Order"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Star Wars Jedi: Fallen Order is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Star Wars Jedi: Fallen Order"
            })
            alanBtnInstance.playText("Star Wars Jedi: Fallen Order has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Watch Dogs 2
    else if (commandData.command === "delete Watch Dogs 2"){
        let game = "Watch Dogs 2"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Watch Dogs 2 is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Watch Dogs 2"
            })
            alanBtnInstance.playText("Watch Dogs 2 has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }
    
    // Phasmophobia
    else if (commandData.command === "delete Phasmophobia"){
        let game = "Phasmophobia"
        let removeornot = false        
        let items = document.querySelectorAll('.item')
        Array.from(items).forEach(item => {
            let itemName = item.children[1].children[0].innerText
            if(itemName == game){
                removeornot = true
            }
        })
        if(removeornot == false){
            alanBtnInstance.playText("Phasmophobia is not in your cart! Please remove something else")
        } else {
            $.ajax({
                type: "GET",
                url: "/shop?delete=true&name=Phasmophobia"
            })
            alanBtnInstance.playText("Phasmophobia has been removed from your cart")
            setTimeout(()=> window.location.reload(), 3000)
        }       
    }

    },
    rootEl: document.getElementById("alan-btn"),
  });
