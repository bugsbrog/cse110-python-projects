# I added a 4th level of choices under INVESTIGATE path. The player decides whether to KEEP or SELL the diamond they found

first_choice = input("You find out you inherited your grandpa's farm and decide to move there. But as soon as you arrive, you notice the farm is a mess. Do you want to start CLEARING the farm or go to TOWN get supplies? ").lower()

if first_choice == "clearing":
    print("You decide to start clearing the farm. You get rid of the plants and trees. You start to hit the rocks with your pickaxe. The rock breaks and a hole suddenly appears.")
    hole_scenario = input("Do you ENTER or IGNORE the hole? ").lower()

    if hole_scenario == "enter":
        print("You decide to enter the hole. You don't know what it leads to... But you can see something glowing, and something coming toward you...")
        mine_choice = input("Do you want to INVESTIGATE the glowing, FIGHT the thing approaching you, or LEAVE? ").lower()

        if mine_choice == "investigate":
            print("You decide to investigate the glowing light. You get closer and see that it is a sparkling diamond! Score! Whatever was approaching you seems to have left.") 
            diamond_choice = input("Do you want to KEEP or SELL the diamond? ").lower()
            if diamond_choice == "keep":
                print("You decide to keep the diamond for later. Who knows? You might need it later...")
            elif diamond_choice == "sell":
                print("You decide to sell the diamond and put it in the shipping bin. You got lots of money from selling it!")
            else:
                print("Please pick one of the words in the story.")
            
        elif mine_choice == "fight":
            print("You square up ready to fight! It turns out to be a slime! You swing at it uncoordinately and manage to kill it, but not before you slip in the slime and fall down, covered in green slime. You won... kind of.")
        elif mine_choice == "leave":
            print("You decide to leave, too scared to find out what's down there... As you climb up the ladder, you hear a bat squeak behind you... You're glad you decided to leave.")
        else:
            print("Please pick one of the words in the story.")

    elif hole_scenario == "ignore":
        print("You decide to leave the hole alone and get back to work on the farm.")
        farm_choice = input("Do you want to PLANT some crops or FIX the old fence? ").lower()

        if farm_choice == "plant":
            print("You decide to plant crops first, feeling excited about growing and harvesting your own plants.")
        elif farm_choice == "fix":
            print("You decide to fix the old fence, and the farm starts feeling more like home.")
        else:
            print("Please pick one of the words in the story.")
    else:
            print("Please pick one of the words in the story.")

elif first_choice == "town":
    print("You decide to head to town to get some supplies. When you get there, you see the grocery store and someone who looks like they want to meet you.")
    town_choice = input("Do you go to the SHOP or TALK to the person? ").lower()

    if town_choice == "shop":
        print("You go into the shop to look for seeds, but there are so many choices!")
        shop_choice = input("Do you choose FRUIT or VEGETABLE seeds? ").lower()

        if shop_choice == "fruit":
            print("You decide on fruit seeds and get some blueberries and melons.")
        elif shop_choice == "vegetable":
            print("You decide on vegetable seeds and get some parsnips, green beans, cauliflowers and potatoes")
        else:
            print("Please pick one of the words in the story.")

    elif town_choice == "talk":
        print("You decide to talk with the person. Her name is Marnie and she sells animals! Good to know when wanting to build a coop and barn!")
        marnie_choice = input("Do you want to ask if she knew GRANDPA or ask about her ANIMALS? ").lower()

        if marnie_choice == "grandpa":
            print("Marnie smiles at you and says your grandpa was always nice to her and would often visit to talk about the farm and buy animals from her.")
        elif marnie_choice == "animals":
            print("Marnie's eyes light up as she tells you all about her chickens, ducks, cows and rabbits and of course, what their names are!")
        else:
            print("Please pick one of the words in the story.")
    else:
        print("Please pick one of the words in the story.")
else:
    print("Please pick one of the words in the story.")
