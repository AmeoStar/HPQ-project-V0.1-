from colorama import Fore
import os
import random      
  


r25KeyText = 'y'


r0 = 'a small cave with a large, ornate doorway filling the far wall'
r1 = 'a tall cave, with icicles hanging in the celing'
r2 = 'a cave split in two by a ravine in the centre'
r3 = 'a dark passage that leads to a small hollow'
r4 = 'a built up stone structure with a treasure chest in it'
r5 = 'a huge cave with ice-covered trees and a half frozen river'
r6 = 'a thin hallway, with water covering the centre '
r7 = 'a hostile looking room, with large icicles on the floor and celing'
r8 = 'a small nook that shows signs of habitation'
r9 = 'a medium sized cave, with an enticing looking pond in the centre'
r10 = 'a large hallway cave, with a few different routes through'
r11 = 'an old garrison, with a few non-rusted weapons on a rack'
r12 = 'a huge cave, with a large depth charge mining setup'
r13 = 'a small cave with an ancient looking key frozen behind ice.'
r14 = 'a smaller hollow, with a stone door to the crypts'
r15 = 'a large war room, with a round table at its centre.'
r16 = 'a large, central area that serves as an entrance to the crypts'
r17 = 'a huge room, with two staircases either side leading to a second floor.'
r18 = 'an old forge, with 3 large containers of lava'
r19 = 'a smaller connecting room, with a gap that shows a long room with pillars'
r20 = 'a room hidden by a painting, inside is a gauntlet of fire that looks quite dangerous'
r21 = 'a winding, connecting passage that has various different murals on the walls'
r22 = 'a side room, with equipment and more murals inside'
r23 = 'a small connecting room'
r24 = 'a huge hallway, lined with pillars, with an impressive statue of a king sits at the far end'
r25 = 'ENTRANCE TO THE CRIMSON CAVES'
r26 = 'STAIRS TO THE CRYPTS'
r27= 'a large central area, with little pitfalls of lava and pillars of ash'
r28= 'a soot covered mine'
r29= 'a large room, with lots of collapsed mineshaft entrances'
r30= 'a half collapsed mineshaft'
r31= 'a large open hall, with lava flowing down the walls'
r32= 'a cartographers hideout'
r33= 'a pool of lava, with small stone columns forming a path across'
r34= 'an ash covered cave with some minecarts stored'
r35= 'a cave passage with minecart tracks running through'
r36= 'a cave dotted with lava pitfalls'
r37= 'a medium sized room with a pool of lava'
r38= 'a long hallway with shifting chains over a pit of spikes'
r39= 'a small connecting cave, covered in ash'
r40= 'a tiny hidden stash of items'
r41= 'a room made of orange sandstone and rocks, with large pillars of rock raised above a magma floor'
r42= 'a tall cave with a dangerous basalt floor'
r43= 'a smaller basalt room, with a skeleton wearing armour in the middle'
r44= 'a long corridor, with many tiles lining the floor and slots in the walls'
r45 = 'a small storage room, with stacked up barrels and bags of gold ore.'
r46 = 'a tiny room dominated by a large hole that stretches down out of sight'
r47 = 'a large, heavily fortified complex made of black stone bricks'
r48 = 'the guards supply room for the prison, containing various weapons'
r49 = 'a hallway, blocked by a trap setup'
r50 = 'a small conecting area of the complex'
r51 = 'the guards hall for the prison, with a collection of scrolls on the wall'
r52 = 'a large, ominous blackstone cave, the prison courtyard area'
r53 = 'a visitors centre for the prison, which looks comfortable'
r54 = 'ENTRANCE TO THE WINDING CAVES'
r55 = 'a long row full of cell blocks, all abandoned.'
r56 = 'a huge, webbed cave with a horrifying clicking noise escaping from hollows within'
r57 = 'a dark passage covered in webs'
r58 = 'a solitary confinement cell, with a dead guard inside'
r59 = 'a series of tunnels getting increasingly smaller in size'
r60 = 'the main cave of the spider domain'
r61 = 'a pitch black room'
r62 = 'ENTRANCE TO THE FUNGAL SYSTEMS'
r63 = 'a luminescent grove of giant, blue mushrooms'
r64 = 'a cave with a stream flowing through the fungal-covered floor'
r65 = 'A built up base with strange sounds echoing from within.'
r66 = 'a large, open forest of fungus'
r67 = 'a stone encampment ruin with campfire smoke rising from within'
r68 = 'a storage area for the encampment'
r69 = 'a shroom-filled passageway'
r70 = 'a small hut built into one of the mushrooms'
r71 = 'a larger house, resembeling a blue pumpkin'
r72 = 'a stone room with a stone door blocking the path forwards'
r73 = 'a misty passageway'
r74 = 'a small, cold cave with heavy smoke covering the floor'
r75 = 'an enourmous cave, with a huge stone bridge'
r76 = 'a densely packed caveway full of winding passages'
r77 = 'a dark set of passages, with water on the floor'
r78 = 'a spiked room full of spiked rocks'
r79 = 'a small hideaway with a cloth draping door'
r80 = 'a long pasageway with walls covered in glowing green gems'
r81 = 'a forked cave, with three total routes'
r82 = 'an entranceway to a chrome building'
r83 = 'a densely packed experiment space, containing various vials'
r84 = 'a room with cords hanging down, conecting to a giant iron suit'
r85 = 'a built up roadway, with warmer mists flowing through'
r86 = 'a large swamp cave, with dark green creepers covering the walls'
r87 = 'a medium sized, swampy cave'
r88 = 'a small connecting cave with dirty water laying on the floor'
r89 = 'a stone ruin'
r90 = 'an elegantly designed rose stone parlour'
r91 = 'a hallway moving further into the parlour'
r92 = 'a small sitting room'
r93 = 'the vault room for the parlour'
r94 = 'a small fishing hut beside a large, flowing river'
r95 = 'the storage shed for the hut'
r96 = 'a large, long passage carved by the rivers flow'
r97 = 'a small room, with a waterfall depositing the river further below'
r98 = 'a more swamp-like area, with flowing waters'
r99 = 'a dark, humid cave'
r100 = 'an open area of swamp with huge vines'
r100tr = 'ENTRANCE TO THE HAUNTED LAKES'



r0d = 'The entrance door to the crypts, it has closed firmly behind you. There is a slot for some kind of device, with patterns that you recognise as belonging to the ancient residents of these caverns. It looks like the artifact you are looking for would fit and open it up again once you recover it from the depths. The rest of the cave is uneventful, if not quite cold.'
r1d = 'This cave is very tall, with its sparkling roof at around 20 metres above your head. The various icicles on the celing dont look as if they will fall anytime soon, but with enough agitation they could become a hazard.'
r2d = 'This cave is a fair bit bigger than the icicle room to its left, though not as tall. The crack that runs through the centre is easy enough to jump over, though the bottom looks quite far down.'
r3d = 'A small, winding corridor that makes your coat stick to the ice somewhat. The small hollow is nothing special, though is noticably warmer than other areas, with some sections showing bedrock rather than ice and snow, perhaps due to the insulation from being this tucked away.'
r4d = 'Quite a basic room, made of cold blocks of stone. various pieces of cloth hang from the walls and in the wooden entrance frame, to keep in a little of the heat. Inside the chest is a map of the crypts and various cartographers tools (not that you can use them.) This appears to be a hideout for a previous adventurer, as a lot of the items look in pretty good condition. The cartographer doesnt seem to be anywhere in sight, however. Perhaps he is hiding further down in the caves.'
r5d = 'A gigantic cave, likely the largest one on this tier of the system. It stretches so high up that the top is out of view, with only a dark shaddow and glowing points of reflection, that give it the appearance of a night sky. Combined with the withered trees now completely frozen and with leaves of snow, the cavern seems to have an ethereal beauty that is both haunting and unnerving. The river is still flowing, though has frozen blocks inside. It poses a serious challenge to jump, though thankfully a half rotting bridge will hold out for the time being.'
r6d = 'There is a slightly hazardous puddle in the centre of the room, that is deceptively deep. Some stalagtites are forming out of the pond, but notably some steel spikes are at the bottom. This appears to have once been a pitfall trap, maybe covered up by snow. It is easy to manouver around it in its current state.'
r7d = 'It is a little tricky to manouver around this room, due to the pillars of ice coming from the floor and celing, making you have to watch your footing. It is easy to miss the small banner door, since it is covered up quite well by the icicles. It seems the passageway to the small nook further down was cut out by hand. The placement of this door seems intentional for stealth. It is unlikely anything large will be able to follow you through to this room.'
r8d = 'This is a small hideout, with a bedspread, desk, and some other personal items. It is covered fully by fabrics and wool insulation, the ice beneath appears to have been melted away. It is surprisingly warm, and a nice respite from the brutal chill of the ice caves. The lantern on the desk catches your eye: it is metal and unscathed by time, in fact it looks quite new. even the wick feels warm still, like it was lit mere hours ago. This place has been used recently, you arent alone in this dungeon.'
r9d = 'Looking down into the pond, you see it is actually more of a cave in its own right, with it going much further down than you would expect. You can see something glinting down at the bottom, but you would have to swim down to get it. Whats even more surprising is that the water is actually very hot, almost like a jacuzzi. It seems to be a heat vent from a cave further down. Youve heard tales of pools of lava in these dungeons, but never gave them credit until now. Could these be from one of these pools?'
r10d = 'There are two seperate hallways that cross over one another a few time over the length of the corridor. It is very long, and seems to connect to rooms around the back side of the crypts.'
r11d = 'This is what appears to be an old outpost for a milita that was protecting the crypt. About a dosen swords line the walls, along with chainmail shirts and iron helmets, though unfortunately the cold and time have ravaged all but one sword, which had fallen among some of the wool fabrics lining the walls and was protected from the worst of the rust, though has seen better days. '
r12d = 'This place catches your eye as important: as it is what appears to be the old entrance to the CRIMSON MINES. You know that venturing down into this area is essential for connecting to even lower parts of the dungeon, but unfortunately it seems to have been blocked off by centuries of collapsing ice and rubble. There is also a depth charge station, that was probably an old project to excavate a second mineshaft down to the second level, but it doesnt appear to have been finished. It is still full with water, and it looks to be empty at the bottom.'
r13d = 'This room is evidently of great significance, you notice. There is a collapsed layer of ice that has melted and fused together to form a translucent wall. Pounding at it with your fists doesnt make a dent or crack, instead just hurting your hand. It doesnt look like any weapons would be strong enough to shatter the ice, at least not on this floor; the depth charges in the next room over could be of use if you could find a way to light them.'
r14d = 'This is a side entrance to the crypts, you can piece together. Some old stone guard posts are at either side of the doorway, which is built directly into the ice and leads further into the dungeon.'
r15d = 'A very large room, it appears to have been important to the ancient peoples who lived in these caverns all those centuries ago. Weirdly, a fire burns in the fireplace, giving the room a warm light, though there isnt any wood in it. The whole place is quite bizare, the wood table and dyes in the cloth are all perfectly intact and vibrant. There is some magic at play in this room, still lingering today. The prospect of what these people were capable of is terrifying; if such a strong spell could last this long, their powers must have been able to raize kingdoms to the ground. After all, this is why the artifact is worth your life to risk.'
r16d = 'It appears that restorative magics are at play throughout this whole building, since it has not been ravaged by time like the other settlements from the time in the ice caves. The whole building is warm, but also has a musty feeling about it that puts you on edge slightly. It certainly isnt a friendly place.'
r17d = 'The twin staircases are leading to a second floor of the crypt, an old doorway lies on the far wall between them but has collapsed and has been completely blocked off. A shame, there are likely many secrets beyond those doorways that you will not experience for now. Perhaps later you could return to this place with proper equipment and explore, though you likely wont find anything that will do the job on this expidition.'
r18d = 'This is what is supplying the building with its heat, you can gather. The three large pots of lava set into the floor were used in the past for forging weapons, but it also seems to have doubled as a radiator of sorts. Magic is likely amplifying the heat, since you can barely think in the roasting atmosphere of the room, which must be at least 40*C or more. Despite this, you can still notice a tinderbox sitting by some old blast furnaces, which were used to light them in the past. Perhaps these could come in useful?'
r19d = 'The room is nothing special, with basic stone lining the walls, but what intrests you is the room further ahead that you can see through a horizontal slit a few inches wide through the wall. You cant make out much, but it certainly seems important and is a prioroty destination.'
r20d = 'The painting, or mural would be the better term since it is a stone carving, has an easy to miss point in the centre that can be pulled out, revealing a door handle. Inside is what looks to be an old servants passage, but now is lit on fire in several places. The fire is static and unmoving, but you know that if you misstep when walking through you could get a nasty burn. Though, it is certainly a safe option for avoiding any unwanted friends.'
r21d = 'Almost maze-like in its design, it turns around at various points, loops and has dead ends. You have no idea what its purpouse was, but what you do know is that these people certainly liked to put pieces of their history here. Multiple murals depicting battles, kings, and various religious events to do with comets and the cosmos line the walls at every turn. You could easily spend hours in this place, but you know you have to press onwards for now.'
r22d = 'Historical scenes line these walls, though instead of the winding passages of the other room, it is a nice, open square. There are various pieces of equipment lying on the ground, a ring, a ruined sword, and most notably leather armour. This looks to be an old cache for another adventurer in these caverns.'
r23d = 'Nothing special about this room, its just a hallway conecting the two rooms either side.'
r24d = 'This room is impressive; row upon row of pillars stretching for around 50 or so metres, a long red carpet all the way up, meeting at the end with a statue of a king, kneeling with a sword resting on his palms. The statue is larger than life, and clearly made to impress with its scale. The sentinal lies dead at your feet, unmoving. Going towards the statue, you see a slot for a key to be inserted into, you can guess that the door behind the statue will open up once you do. You can gather that this statue is a grave for the king it depicts.'
r25d = 'Looks like you need a key to pass through the door. '
r26d='The staircase connects back up to the Crypts, where the cold ice still blows through, but on the other side an intense heat resides.'
r27d='The cave is huge, with pillared stacks stretching up to the celing all throughout, and a brimstone haze lingering around the pitfalls of scorching liquid. A minehouse lies to your left, and more brimstone caves to your right.'
r28d='The entrance to the minehouse is fairly large, with crossbeams of steel to weather the heat. various piles of ore lie around the floor.'
r29d='The large centre of the minehouse, the mines that stretched off from them having caved in from time weather. Racks with mining equipment remains fairly preserved, including a pickaxe'
r30d='The walls to this mineshaft have also nearly collapsed, but a small hollow leads you through to a room further on'
r31d='A hidden cave that was found and used by the miners. They dug out entrances to points further ahead in the cave system. There is a sub-room partially obscured by a lava collum south of you.'
r32d='A small hollow with similar drapings to the map room on the last floor. This room too contains a map, lying amongst others in a pile on a table. This looks like a comfortable place to rest.'
r33d='A room flooded with lava, but some thick bars of metal you dont recognise, with a blue shine to them, sticking out of the floor. Flowing lava currents cover up certain bars, so it is difficult to traverse.'
r34d='The minecarts are piled up against the cave wall, out of the way.'
r35d='The minecart tracks appear to lead to now collapsed pathways to caves further beyond. Some lead to the other rooms you can access.'
r36d='The lava pitfalls arent much of an issue to traverse when not under pressure.'
r37d='The pool of lava releases a superheated steam to some cracks in the cave celing. Based on where you are in relation to the first layer, you judge that you are below the hot spring. A scroll sits on a stone bench.'
r38d='There is one long chain that is pulled taught across to the other side of the room. There are chains at various points along the larger one, with a mechanism still whiring, likely magically, pulling the chain in various directions.'
r39d='The room ahead is covered in pillars, some of them spreading into the room you are in.'
r40d='A small room with a little treasure hoard piled neatly in a stone drawer, along with other recently made improvements.'
r41d='The pillars are roughly 4 or so metres tall, and are dotted extremely frequently around the room. The floor below is made of rocks, with flowing cracks of lava between them. It looks painful to traverse.'
r42d='Ash and crumbing rock makes up the cave, and the floor has several holes in it, leading to darkness. You will have to tread carefuly.'
r43d='The skeleton is wearing chainmail of good quality metal, but it has taken a fair bit of damage, with a few holes burned into the links in places.'
r44d='By throwing a stone at the floor, you realise that some of the tiles trigger an arrow to shoot out of the slot. It is hard to tell which tiles are safe.'
r45d='A little sub-room connecting off of the stacks room to the south. The barrels contain coal and other ores, and some treasure can be found in the gold pile.'
r46d='The hole isnt much of an issue as there is a good bit of room around it. There are two pathways to take here, to the east is a built up complex, and to the west, a dimly lit cave covered with cobwebs.'
r47d='This is a large, central room for the fortress, it appears abandoned as there are no guards posted, and the cell doors to the north are all open.'
r48d='The weapon racks are well maintained, some good quality steel swords can be found and used. This looks to be a recently used supply location'
r49d='The trap is more of a set of wires, rigged up to the celing. If triggered they could make it collapse in that section. It seems to have been set up recently.'
r50d='A regular hallway, there are sets of heavy iron doors that would have been imposing in the past, but have rusted off their hinges.'
r51d='The guards hall has a long, now rotten wooden table for eating, as well as a stone bookshelves for their scrolls. They contain the spell Tesla Coil within them, something that would have been used to subdue unruly prisoners.'
r52d='Some old exercise equipment, and a pump for pulling water rest in this courtyard.'
r53d='You should be able to rest on the matress, while it is old it is still surprisingly clean and well kept.'
r54d='Ahead of you is a dark, twisting cave system.'
r55d='There are several rows of cells in place, most of which are empty but for one, which has a small vial containing a potion lying on the floor.'
r56d='It is difficult to move through the cave, as the webs stop you in your tracks and force you to struggle through every time you pass through them. You have an unnerving feeling of being watched.'
r57d='A small passageway, you can see little bugs crawling allong the floor, their shaddows dancing to the wick of your lantern.'
r58d='The solitary confinement cell has a similar design to the fortress to the east, and the guards skeleton is wearing mail, that is relatively intact.'
r59d='The tunnels are winding, and very unnerving. There is a central area in the room, which is also quite small.'
r60d='The lair is exeptionally dark, the clicking noises become deafaning as you enter. Lots of movement just beyond your vision scuttles on the celing.'
r61d='You cannot see more than a few feet in front of you, even with the lantern.'
r62d='Ahead is a glowing, blue forrest, that appears almost unnatural and yet not entirely uninviting at the same time.'
r63d = ' '
r64d = ' '
r65d = ' '
r66d = ' '
r67d = ' '
r68d = ' '
r69d = ' '
r70d = ' '
r71d = ' '
r72d = ' '
r73d = ' '
r74d = ' '
r75d = ' '
r76d = ' '
r77d = ' '
r78d = ' '
r79d = ' '
r80d = ' '
r81d = ' '
r82d = ' '
r83d = ' '
r84d = ' '
r85d = ' '
r86d = ' '
r87d = ' '
r88d = ' '
r89d = ' '
r90d = ' '
r91d = ' '
r92d = ' '
r93d = ' '
r94d = ' '
r95d = ' '
r96d = ' '
r97d = ' '
r98d = ' '
r99d = ' '
r100d = ' '
r100trd = ' '

Nbm   = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

r5BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1]]

r24BM = [[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]

r35BM=  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
         
r29BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r46BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r50BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r52BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
         [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r55BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r57BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r59BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r60BM =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 1, 1, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1]]








#      ---IMPORTANT---   This code is not mine, I have instead adapted it to give me the output I want from it, being the next tile.   The source code has been cited in the bibliography of my project.    I AM NOT TRYING TO PASS THIS CODE OFF AS MINE, ALL CREDIT GOES TO THE AUTHOR (its a very nice program btw)
class Node():
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position
def astar(maze, start, end, enemy, type, enemy2):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)
    # Add the start node
    open_list.append(start_node)
    # Loop until you find the end
    while len(open_list) > 0:
      outer_iterations += 1
      if outer_iterations > max_iterations:
        break
      # Get the current node
      current_node = open_list[0]
      current_index = 0
      for index, item in enumerate(open_list):
          if item.f < current_node.f:
              current_node = item
              current_index = index
      # Pop current off open list, add to closed list
      open_list.pop(current_index)
      closed_list.append(current_node)
      # Found the goal
      if current_node == end_node:
          path = []
          current = current_node
          while current is not None:
              path.append(current.position)
              current = current.parent
          path = path[::-1] # reverse path
          nextT = path[1]            
          enemy.ETile = nextT[1] + nextT[0] * 20
          break
          
      # Generate children
      children = []
      for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
          # Get node position
          node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
          # Make sure within range
          if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
              continue
          # Make sure walkable terrain
          if maze[node_position[0]][node_position[1]] != 0:
              continue
          if type == 2:
            if maze
          # Create new node
          new_node = Node(current_node, node_position)
          # Append
          children.append(new_node)
      # Loop through children
      for child in children:
          # Child is on the closed list
          for closed_child in closed_list:
              if child == closed_child:
                  continue
          # Create the f, g, and h values
          child.g = current_node.g + 1
          child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
          child.f = child.g + child.h
          # Child is already in the open list
          for open_node in open_list:
              if child == open_node and child.g > open_node.g:
                  continue
          # Add the child to the open list
          open_list.append(child)

        





def battlemap():
  print(Fore.RESET)
  print("##########################################")
  print( "#" +  screen[0]['display'] +   screen[1]['display'] +   screen[2]['display'] +   screen[3]['display'] +   screen[4]['display'] +   screen[5]['display'] +   screen[6]['display'] +   screen[7]['display'] +   screen[8]['display'] +   screen[9]['display'] +  screen[10]['display'] +  screen[11]['display'] +  screen[12]['display'] +  screen[13]['display'] +  screen[14]['display'] +  screen[15]['display'] +  screen[16]['display'] +  screen[17]['display'] +  screen[18]['display'] +  screen[19]['display'] + "#")
  print( "#" + screen[20]['display'] +  screen[21]['display'] +  screen[22]['display'] +  screen[23]['display'] +  screen[24]['display'] +  screen[25]['display'] +  screen[26]['display'] +  screen[27]['display'] +  screen[28]['display'] +  screen[29]['display'] +  screen[30]['display'] +  screen[31]['display'] +  screen[32]['display'] +  screen[33]['display'] +  screen[34]['display'] +  screen[35]['display'] +  screen[36]['display'] +  screen[37]['display'] +  screen[38]['display'] +  screen[39]['display'] + "#")
  print( "#" + screen[40]['display'] +  screen[41]['display'] +  screen[42]['display'] +  screen[43]['display'] +  screen[44]['display'] +  screen[45]['display'] +  screen[46]['display'] +  screen[47]['display'] +  screen[48]['display'] +  screen[49]['display'] +  screen[50]['display'] +  screen[51]['display'] +  screen[52]['display'] +  screen[53]['display'] +  screen[54]['display'] +  screen[55]['display'] +  screen[56]['display'] +  screen[57]['display'] +  screen[58]['display'] +  screen[59]['display'] + "#")
  print( "#" + screen[60]['display'] +  screen[61]['display'] +  screen[62]['display'] +  screen[63]['display'] +  screen[64]['display'] +  screen[65]['display'] +  screen[66]['display'] +  screen[67]['display'] +  screen[68]['display'] +  screen[69]['display'] +  screen[70]['display'] +  screen[71]['display'] +  screen[72]['display'] +  screen[73]['display'] +  screen[74]['display'] +  screen[75]['display'] +  screen[76]['display'] +  screen[77]['display'] +  screen[78]['display'] +  screen[79]['display'] + "#")
  print( "#" + screen[80]['display'] +  screen[81]['display'] +  screen[82]['display'] +  screen[83]['display'] +  screen[84]['display'] +  screen[85]['display'] +  screen[86]['display'] +  screen[87]['display'] +  screen[88]['display'] +  screen[89]['display'] +  screen[90]['display'] +  screen[91]['display'] +  screen[92]['display'] +  screen[93]['display'] +  screen[94]['display'] +  screen[95]['display'] +  screen[96]['display'] +  screen[97]['display'] +  screen[98]['display'] +  screen[99]['display'] + "#")
  print("#" + screen[100]['display'] + screen[101]['display'] + screen[102]['display'] + screen[103]['display'] + screen[104]['display'] + screen[105]['display'] + screen[106]['display'] + screen[107]['display'] + screen[108]['display'] + screen[109]['display'] + screen[110]['display'] + screen[111]['display'] + screen[112]['display'] + screen[113]['display'] + screen[114]['display'] + screen[115]['display'] + screen[116]['display'] + screen[117]['display'] + screen[118]['display'] + screen[119]['display'] + "#")
  print("#" + screen[120]['display'] + screen[121]['display'] + screen[122]['display'] + screen[123]['display'] + screen[124]['display'] + screen[125]['display'] + screen[126]['display'] + screen[127]['display'] + screen[128]['display'] + screen[129]['display'] + screen[130]['display'] + screen[131]['display'] + screen[132]['display'] + screen[133]['display'] + screen[134]['display'] + screen[135]['display'] + screen[136]['display'] + screen[137]['display'] + screen[138]['display'] + screen[139]['display'] + "#")
  print("#" + screen[140]['display'] + screen[141]['display'] + screen[142]['display'] + screen[143]['display'] + screen[144]['display'] + screen[145]['display'] + screen[146]['display'] + screen[147]['display'] + screen[148]['display'] + screen[149]['display'] + screen[150]['display'] + screen[151]['display'] + screen[152]['display'] + screen[153]['display'] + screen[154]['display'] + screen[155]['display'] + screen[156]['display'] + screen[157]['display'] + screen[158]['display'] + screen[159]['display'] + "#")
  print("#" + screen[160]['display'] + screen[161]['display'] + screen[162]['display'] + screen[163]['display'] + screen[164]['display'] + screen[165]['display'] + screen[166]['display'] + screen[167]['display'] + screen[168]['display'] + screen[169]['display'] + screen[170]['display'] + screen[171]['display'] + screen[172]['display'] + screen[173]['display'] + screen[174]['display'] + screen[175]['display'] + screen[176]['display'] + screen[177]['display'] + screen[178]['display'] + screen[179]['display'] + "#")
  print("#" + screen[180]['display'] + screen[181]['display'] + screen[182]['display'] + screen[183]['display'] + screen[184]['display'] + screen[185]['display'] + screen[186]['display'] + screen[187]['display'] + screen[188]['display'] + screen[189]['display'] + screen[190]['display'] + screen[191]['display'] + screen[192]['display'] + screen[193]['display'] + screen[194]['display'] + screen[195]['display'] + screen[196]['display'] + screen[197]['display'] + screen[198]['display'] + screen[199]['display'] + "#")
  print("#" + screen[200]['display'] + screen[201]['display'] + screen[202]['display'] + screen[203]['display'] + screen[204]['display'] + screen[205]['display'] + screen[206]['display'] + screen[207]['display'] + screen[208]['display'] + screen[209]['display'] + screen[210]['display'] + screen[211]['display'] + screen[212]['display'] + screen[213]['display'] + screen[214]['display'] + screen[215]['display'] + screen[216]['display'] + screen[217]['display'] + screen[218]['display'] + screen[219]['display'] + "#")
  print("#" + screen[220]['display'] + screen[221]['display'] + screen[222]['display'] + screen[223]['display'] + screen[224]['display'] + screen[225]['display'] + screen[226]['display'] + screen[227]['display'] + screen[228]['display'] + screen[229]['display'] + screen[230]['display'] + screen[231]['display'] + screen[232]['display'] + screen[233]['display'] + screen[234]['display'] + screen[235]['display'] + screen[236]['display'] + screen[237]['display'] + screen[238]['display'] + screen[239]['display'] + "#")
  print("#" + screen[240]['display'] + screen[241]['display'] + screen[242]['display'] + screen[243]['display'] + screen[244]['display'] + screen[245]['display'] + screen[246]['display'] + screen[247]['display'] + screen[248]['display'] + screen[249]['display'] + screen[250]['display'] + screen[251]['display'] + screen[252]['display'] + screen[253]['display'] + screen[254]['display'] + screen[255]['display'] + screen[256]['display'] + screen[257]['display'] + screen[258]['display'] + screen[259]['display'] + "#")
  print("#" + screen[260]['display'] + screen[261]['display'] + screen[262]['display'] + screen[263]['display'] + screen[264]['display'] + screen[265]['display'] + screen[266]['display'] + screen[267]['display'] + screen[268]['display'] + screen[269]['display'] + screen[270]['display'] + screen[271]['display'] + screen[272]['display'] + screen[273]['display'] + screen[274]['display'] + screen[275]['display'] + screen[276]['display'] + screen[277]['display'] + screen[278]['display'] + screen[279]['display'] + "#")
  print("#" + screen[280]['display'] + screen[281]['display'] + screen[282]['display'] + screen[283]['display'] + screen[284]['display'] + screen[285]['display'] + screen[286]['display'] + screen[287]['display'] + screen[288]['display'] + screen[289]['display'] + screen[290]['display'] + screen[291]['display'] + screen[292]['display'] + screen[293]['display'] + screen[294]['display'] + screen[295]['display'] + screen[296]['display'] + screen[297]['display'] + screen[298]['display'] + screen[299]['display'] + "#")
  print("#" + screen[300]['display'] + screen[301]['display'] + screen[302]['display'] + screen[303]['display'] + screen[304]['display'] + screen[305]['display'] + screen[306]['display'] + screen[307]['display'] + screen[308]['display'] + screen[309]['display'] + screen[310]['display'] + screen[311]['display'] + screen[312]['display'] + screen[313]['display'] + screen[314]['display'] + screen[315]['display'] + screen[316]['display'] + screen[317]['display'] + screen[318]['display'] + screen[319]['display'] + "#")
  print("#" + screen[320]['display'] + screen[321]['display'] + screen[322]['display'] + screen[323]['display'] + screen[324]['display'] + screen[325]['display'] + screen[326]['display'] + screen[327]['display'] + screen[328]['display'] + screen[329]['display'] + screen[330]['display'] + screen[331]['display'] + screen[332]['display'] + screen[333]['display'] + screen[334]['display'] + screen[335]['display'] + screen[336]['display'] + screen[337]['display'] + screen[338]['display'] + screen[339]['display'] + "#")
  print("#" + screen[340]['display'] + screen[341]['display'] + screen[342]['display'] + screen[343]['display'] + screen[344]['display'] + screen[345]['display'] + screen[346]['display'] + screen[347]['display'] + screen[348]['display'] + screen[349]['display'] + screen[350]['display'] + screen[351]['display'] + screen[352]['display'] + screen[353]['display'] + screen[354]['display'] + screen[355]['display'] + screen[356]['display'] + screen[357]['display'] + screen[358]['display'] + screen[359]['display'] + "#")
  print("#" + screen[360]['display'] + screen[361]['display'] + screen[362]['display'] + screen[363]['display'] + screen[364]['display'] + screen[365]['display'] + screen[366]['display'] + screen[367]['display'] + screen[368]['display'] + screen[369]['display'] + screen[370]['display'] + screen[371]['display'] + screen[372]['display'] + screen[373]['display'] + screen[374]['display'] + screen[375]['display'] + screen[376]['display'] + screen[377]['display'] + screen[378]['display'] + screen[379]['display'] + "#")
  print("#" + screen[380]['display'] + screen[381]['display'] + screen[382]['display'] + screen[383]['display'] + screen[384]['display'] + screen[385]['display'] + screen[386]['display'] + screen[387]['display'] + screen[388]['display'] + screen[389]['display'] + screen[390]['display'] + screen[391]['display'] + screen[392]['display'] + screen[393]['display'] + screen[394]['display'] + screen[395]['display'] + screen[396]['display'] + screen[397]['display'] + screen[398]['display'] + screen[399]['display'] + "#")
  print("##########################################")


screen = {
   0:{'num':0,'display':'  ','x':0,'y':0,},
   1:{'num':0,'display':'  ','x':0,'y':0,},
   2:{'num':0,'display':'  ','x':0,'y':0,},
   3:{'num':0,'display':'  ','x':0,'y':0,},
   4:{'num':0,'display':'  ','x':0,'y':0,},
   5:{'num':0,'display':'  ','x':0,'y':0,},
   6:{'num':0,'display':'  ','x':0,'y':0,},
   7:{'num':0,'display':'  ','x':0,'y':0,},
   8:{'num':0,'display':'  ','x':0,'y':0,},
   9:{'num':0,'display':'  ','x':0,'y':0,},
   10:{'num':0,'display':'  ','x':0,'y':0,},
   11:{'num':0,'display':'  ','x':0,'y':0,},
   12:{'num':0,'display':'  ','x':0,'y':0,},
   13:{'num':0,'display':'  ','x':0,'y':0,},
   14:{'num':0,'display':'  ','x':0,'y':0,},
   15:{'num':0,'display':'  ','x':0,'y':0,},
   16:{'num':0,'display':'  ','x':0,'y':0,},
   17:{'num':0,'display':'  ','x':0,'y':0,},
   18:{'num':0,'display':'  ','x':0,'y':0,},
   19:{'num':0,'display':'  ','x':0,'y':0,},
   20:{'num':0,'display':'  ','x':0,'y':0,},
   21:{'num':0,'display':'  ','x':0,'y':0,},
   22:{'num':0,'display':'  ','x':0,'y':0,},
   23:{'num':0,'display':'  ','x':0,'y':0,},
   24:{'num':0,'display':'  ','x':0,'y':0,},
   25:{'num':0,'display':'  ','x':0,'y':0,},
   26:{'num':0,'display':'  ','x':0,'y':0,},
   27:{'num':0,'display':'  ','x':0,'y':0,},
   28:{'num':0,'display':'  ','x':0,'y':0,},
   29:{'num':0,'display':'  ','x':0,'y':0,},
   30:{'num':0,'display':'  ','x':0,'y':0,},
   31:{'num':0,'display':'  ','x':0,'y':0,},
   32:{'num':0,'display':'  ','x':0,'y':0,},
   33:{'num':0,'display':'  ','x':0,'y':0,},
   34:{'num':0,'display':'  ','x':0,'y':0,},
   35:{'num':0,'display':'  ','x':0,'y':0,},
   36:{'num':0,'display':'  ','x':0,'y':0,},
   37:{'num':0,'display':'  ','x':0,'y':0,},
   38:{'num':0,'display':'  ','x':0,'y':0,},
   39:{'num':0,'display':'  ','x':0,'y':0,},
   40:{'num':0,'display':'  ','x':0,'y':0,},
   41:{'num':0,'display':'  ','x':0,'y':0,},
   42:{'num':0,'display':'  ','x':0,'y':0,},
   43:{'num':0,'display':'  ','x':0,'y':0,},
   44:{'num':0,'display':'  ','x':0,'y':0,},
   45:{'num':0,'display':'  ','x':0,'y':0,},
   46:{'num':0,'display':'  ','x':0,'y':0,},
   47:{'num':0,'display':'  ','x':0,'y':0,},
   48:{'num':0,'display':'  ','x':0,'y':0,},
   49:{'num':0,'display':'  ','x':0,'y':0,},
   50:{'num':0,'display':'  ','x':0,'y':0,},
   51:{'num':0,'display':'  ','x':0,'y':0,},
   52:{'num':0,'display':'  ','x':0,'y':0,},
   53:{'num':0,'display':'  ','x':0,'y':0,},
   54:{'num':0,'display':'  ','x':0,'y':0,},
   55:{'num':0,'display':'  ','x':0,'y':0,},
   56:{'num':0,'display':'  ','x':0,'y':0,},
   57:{'num':0,'display':'  ','x':0,'y':0,},
   58:{'num':0,'display':'  ','x':0,'y':0,},
   59:{'num':0,'display':'  ','x':0,'y':0,},
   60:{'num':0,'display':'  ','x':0,'y':0,},
   61:{'num':0,'display':'  ','x':0,'y':0,},
   62:{'num':0,'display':'  ','x':0,'y':0,},
   63:{'num':0,'display':'  ','x':0,'y':0,},
   64:{'num':0,'display':'  ','x':0,'y':0,},
   65:{'num':0,'display':'  ','x':0,'y':0,},
   66:{'num':0,'display':'  ','x':0,'y':0,},
   67:{'num':0,'display':'  ','x':0,'y':0,},
   68:{'num':0,'display':'  ','x':0,'y':0,},
   69:{'num':0,'display':'  ','x':0,'y':0,},
   70:{'num':0,'display':'  ','x':0,'y':0,},
   71:{'num':0,'display':'  ','x':0,'y':0,},
   72:{'num':0,'display':'  ','x':0,'y':0,},
   73:{'num':0,'display':'  ','x':0,'y':0,},
   74:{'num':0,'display':'  ','x':0,'y':0,},
   75:{'num':0,'display':'  ','x':0,'y':0,},
   76:{'num':0,'display':'  ','x':0,'y':0,},
   77:{'num':0,'display':'  ','x':0,'y':0,},
   78:{'num':0,'display':'  ','x':0,'y':0,},
   79:{'num':0,'display':'  ','x':0,'y':0,},
   80:{'num':0,'display':'  ','x':0,'y':0,},
   81:{'num':0,'display':'  ','x':0,'y':0,},
   82:{'num':0,'display':'  ','x':0,'y':0,},
   83:{'num':0,'display':'  ','x':0,'y':0,},
   84:{'num':0,'display':'  ','x':0,'y':0,},
   85:{'num':0,'display':'  ','x':0,'y':0,},
   86:{'num':0,'display':'  ','x':0,'y':0,},
   87:{'num':0,'display':'  ','x':0,'y':0,},
   88:{'num':0,'display':'  ','x':0,'y':0,},
   89:{'num':0,'display':'  ','x':0,'y':0,},
   90:{'num':0,'display':'  ','x':0,'y':0,},
   91:{'num':0,'display':'  ','x':0,'y':0,},
   92:{'num':0,'display':'  ','x':0,'y':0,},
   93:{'num':0,'display':'  ','x':0,'y':0,},
   94:{'num':0,'display':'  ','x':0,'y':0,},
   95:{'num':0,'display':'  ','x':0,'y':0,},
   96:{'num':0,'display':'  ','x':0,'y':0,},
   97:{'num':0,'display':'  ','x':0,'y':0,},
   98:{'num':0,'display':'  ','x':0,'y':0,},
   99:{'num':0,'display':'  ','x':0,'y':0,},
   100:{'num':0,'display':'  ','x':0,'y':0,},
   101:{'num':0,'display':'  ','x':0,'y':0,},
   102:{'num':0,'display':'  ','x':0,'y':0,},
   103:{'num':0,'display':'  ','x':0,'y':0,},
   104:{'num':0,'display':'  ','x':0,'y':0,},
   105:{'num':0,'display':'  ','x':0,'y':0,},
   106:{'num':0,'display':'  ','x':0,'y':0,},
   107:{'num':0,'display':'  ','x':0,'y':0,},
   108:{'num':0,'display':'  ','x':0,'y':0,},
   109:{'num':0,'display':'  ','x':0,'y':0,},
   110:{'num':0,'display':'  ','x':0,'y':0,},
   111:{'num':0,'display':'  ','x':0,'y':0,},
   112:{'num':0,'display':'  ','x':0,'y':0,},
   113:{'num':0,'display':'  ','x':0,'y':0,},
   114:{'num':0,'display':'  ','x':0,'y':0,},
   115:{'num':0,'display':'  ','x':0,'y':0,},
   116:{'num':0,'display':'  ','x':0,'y':0,},
   117:{'num':0,'display':'  ','x':0,'y':0,},
   118:{'num':0,'display':'  ','x':0,'y':0,},
   119:{'num':0,'display':'  ','x':0,'y':0,},
   120:{'num':0,'display':'  ','x':0,'y':0,},
   121:{'num':0,'display':'  ','x':0,'y':0,},
   122:{'num':0,'display':'  ','x':0,'y':0,},
   123:{'num':0,'display':'  ','x':0,'y':0,},
   124:{'num':0,'display':'  ','x':0,'y':0,},
   125:{'num':0,'display':'  ','x':0,'y':0,},
   126:{'num':0,'display':'  ','x':0,'y':0,},
   127:{'num':0,'display':'  ','x':0,'y':0,},
   128:{'num':0,'display':'  ','x':0,'y':0,},
   129:{'num':0,'display':'  ','x':0,'y':0,},
   130:{'num':0,'display':'  ','x':0,'y':0,},
   131:{'num':0,'display':'  ','x':0,'y':0,},
   132:{'num':0,'display':'  ','x':0,'y':0,},
   133:{'num':0,'display':'  ','x':0,'y':0,},
   134:{'num':0,'display':'  ','x':0,'y':0,},
   135:{'num':0,'display':'  ','x':0,'y':0,},
   136:{'num':0,'display':'  ','x':0,'y':0,},
   137:{'num':0,'display':'  ','x':0,'y':0,},
   138:{'num':0,'display':'  ','x':0,'y':0,},
   139:{'num':0,'display':'  ','x':0,'y':0,},
   140:{'num':0,'display':'  ','x':0,'y':0,},
   141:{'num':0,'display':'  ','x':0,'y':0,},
   142:{'num':0,'display':'  ','x':0,'y':0,},
   143:{'num':0,'display':'  ','x':0,'y':0,},
   144:{'num':0,'display':'  ','x':0,'y':0,},
   145:{'num':0,'display':'  ','x':0,'y':0,},
   146:{'num':0,'display':'  ','x':0,'y':0,},
   147:{'num':0,'display':'  ','x':0,'y':0,},
   148:{'num':0,'display':'  ','x':0,'y':0,},
   149:{'num':0,'display':'  ','x':0,'y':0,},
   150:{'num':0,'display':'  ','x':0,'y':0,},
   151:{'num':0,'display':'  ','x':0,'y':0,},
   152:{'num':0,'display':'  ','x':0,'y':0,},
   153:{'num':0,'display':'  ','x':0,'y':0,},
   154:{'num':0,'display':'  ','x':0,'y':0,},
   155:{'num':0,'display':'  ','x':0,'y':0,},
   156:{'num':0,'display':'  ','x':0,'y':0,},
   157:{'num':0,'display':'  ','x':0,'y':0,},
   158:{'num':0,'display':'  ','x':0,'y':0,},
   159:{'num':0,'display':'  ','x':0,'y':0,},
   160:{'num':0,'display':'  ','x':0,'y':0,},
   161:{'num':0,'display':'  ','x':0,'y':0,},
   162:{'num':0,'display':'  ','x':0,'y':0,},
   163:{'num':0,'display':'  ','x':0,'y':0,},
   164:{'num':0,'display':'  ','x':0,'y':0,},
   165:{'num':0,'display':'  ','x':0,'y':0,},
   166:{'num':0,'display':'  ','x':0,'y':0,},
   167:{'num':0,'display':'  ','x':0,'y':0,},
   168:{'num':0,'display':'  ','x':0,'y':0,},
   169:{'num':0,'display':'  ','x':0,'y':0,},
   170:{'num':0,'display':'  ','x':0,'y':0,},
   171:{'num':0,'display':'  ','x':0,'y':0,},
   172:{'num':0,'display':'  ','x':0,'y':0,},
   173:{'num':0,'display':'  ','x':0,'y':0,},
   174:{'num':0,'display':'  ','x':0,'y':0,},
   175:{'num':0,'display':'  ','x':0,'y':0,},
   176:{'num':0,'display':'  ','x':0,'y':0,},
   177:{'num':0,'display':'  ','x':0,'y':0,},
   178:{'num':0,'display':'  ','x':0,'y':0,},
   179:{'num':0,'display':'  ','x':0,'y':0,},
   180:{'num':0,'display':'  ','x':0,'y':0,},
   181:{'num':0,'display':'  ','x':0,'y':0,},
   182:{'num':0,'display':'  ','x':0,'y':0,},
   183:{'num':0,'display':'  ','x':0,'y':0,},
   184:{'num':0,'display':'  ','x':0,'y':0,},
   185:{'num':0,'display':'  ','x':0,'y':0,},
   186:{'num':0,'display':'  ','x':0,'y':0,},
   187:{'num':0,'display':'  ','x':0,'y':0,},
   188:{'num':0,'display':'  ','x':0,'y':0,},
   189:{'num':0,'display':'  ','x':0,'y':0,},
   190:{'num':0,'display':'  ','x':0,'y':0,},
   191:{'num':0,'display':'  ','x':0,'y':0,},
   192:{'num':0,'display':'  ','x':0,'y':0,},
   193:{'num':0,'display':'  ','x':0,'y':0,},
   194:{'num':0,'display':'  ','x':0,'y':0,},
   195:{'num':0,'display':'  ','x':0,'y':0,},
   196:{'num':0,'display':'  ','x':0,'y':0,},
   197:{'num':0,'display':'  ','x':0,'y':0,},
   198:{'num':0,'display':'  ','x':0,'y':0,},
   199:{'num':0,'display':'  ','x':0,'y':0,},
   200:{'num':0,'display':'  ','x':0,'y':0,},
   201:{'num':0,'display':'  ','x':0,'y':0,},
   202:{'num':0,'display':'  ','x':0,'y':0,},
   203:{'num':0,'display':'  ','x':0,'y':0,},
   204:{'num':0,'display':'  ','x':0,'y':0,},
   205:{'num':0,'display':'  ','x':0,'y':0,},
   206:{'num':0,'display':'  ','x':0,'y':0,},
   207:{'num':0,'display':'  ','x':0,'y':0,},
   208:{'num':0,'display':'  ','x':0,'y':0,},
   209:{'num':0,'display':'  ','x':0,'y':0,},
   210:{'num':0,'display':'  ','x':0,'y':0,},
   211:{'num':0,'display':'  ','x':0,'y':0,},
   212:{'num':0,'display':'  ','x':0,'y':0,},
   213:{'num':0,'display':'  ','x':0,'y':0,},
   214:{'num':0,'display':'  ','x':0,'y':0,},
   215:{'num':0,'display':'  ','x':0,'y':0,},
   216:{'num':0,'display':'  ','x':0,'y':0,},
   217:{'num':0,'display':'  ','x':0,'y':0,},
   218:{'num':0,'display':'  ','x':0,'y':0,},
   219:{'num':0,'display':'  ','x':0,'y':0,},
   220:{'num':0,'display':'  ','x':0,'y':0,},
   221:{'num':0,'display':'  ','x':0,'y':0,},
   222:{'num':0,'display':'  ','x':0,'y':0,},
   223:{'num':0,'display':'  ','x':0,'y':0,},
   224:{'num':0,'display':'  ','x':0,'y':0,},
   225:{'num':0,'display':'  ','x':0,'y':0,},
   226:{'num':0,'display':'  ','x':0,'y':0,},
   227:{'num':0,'display':'  ','x':0,'y':0,},
   228:{'num':0,'display':'  ','x':0,'y':0,},
   229:{'num':0,'display':'  ','x':0,'y':0,},
   230:{'num':0,'display':'  ','x':0,'y':0,},
   231:{'num':0,'display':'  ','x':0,'y':0,},
   232:{'num':0,'display':'  ','x':0,'y':0,},
   233:{'num':0,'display':'  ','x':0,'y':0,},
   234:{'num':0,'display':'  ','x':0,'y':0,},
   235:{'num':0,'display':'  ','x':0,'y':0,},
   236:{'num':0,'display':'  ','x':0,'y':0,},
   237:{'num':0,'display':'  ','x':0,'y':0,},
   238:{'num':0,'display':'  ','x':0,'y':0,},
   239:{'num':0,'display':'  ','x':0,'y':0,},
   240:{'num':0,'display':'  ','x':0,'y':0,},
   241:{'num':0,'display':'  ','x':0,'y':0,},
   242:{'num':0,'display':'  ','x':0,'y':0,},
   243:{'num':0,'display':'  ','x':0,'y':0,},
   244:{'num':0,'display':'  ','x':0,'y':0,},
   245:{'num':0,'display':'  ','x':0,'y':0,},
   246:{'num':0,'display':'  ','x':0,'y':0,},
   247:{'num':0,'display':'  ','x':0,'y':0,},
   248:{'num':0,'display':'  ','x':0,'y':0,},
   249:{'num':0,'display':'  ','x':0,'y':0,},
   250:{'num':0,'display':'  ','x':0,'y':0,},
   251:{'num':0,'display':'  ','x':0,'y':0,},
   252:{'num':0,'display':'  ','x':0,'y':0,},
   253:{'num':0,'display':'  ','x':0,'y':0,},
   254:{'num':0,'display':'  ','x':0,'y':0,},
   255:{'num':0,'display':'  ','x':0,'y':0,},
   256:{'num':0,'display':'  ','x':0,'y':0,},
   257:{'num':0,'display':'  ','x':0,'y':0,},
   258:{'num':0,'display':'  ','x':0,'y':0,},
   259:{'num':0,'display':'  ','x':0,'y':0,},
   260:{'num':0,'display':'  ','x':0,'y':0,},
   261:{'num':0,'display':'  ','x':0,'y':0,},
   262:{'num':0,'display':'  ','x':0,'y':0,},
   263:{'num':0,'display':'  ','x':0,'y':0,},
   264:{'num':0,'display':'  ','x':0,'y':0,},
   265:{'num':0,'display':'  ','x':0,'y':0,},
   266:{'num':0,'display':'  ','x':0,'y':0,},
   267:{'num':0,'display':'  ','x':0,'y':0,},
   268:{'num':0,'display':'  ','x':0,'y':0,},
   269:{'num':0,'display':'  ','x':0,'y':0,},
   270:{'num':0,'display':'  ','x':0,'y':0,},
   271:{'num':0,'display':'  ','x':0,'y':0,},
   272:{'num':0,'display':'  ','x':0,'y':0,},
   273:{'num':0,'display':'  ','x':0,'y':0,},
   274:{'num':0,'display':'  ','x':0,'y':0,},
   275:{'num':0,'display':'  ','x':0,'y':0,},
   276:{'num':0,'display':'  ','x':0,'y':0,},
   277:{'num':0,'display':'  ','x':0,'y':0,},
   278:{'num':0,'display':'  ','x':0,'y':0,},
   279:{'num':0,'display':'  ','x':0,'y':0,},
   280:{'num':0,'display':'  ','x':0,'y':0,},
   281:{'num':0,'display':'  ','x':0,'y':0,},
   282:{'num':0,'display':'  ','x':0,'y':0,},
   283:{'num':0,'display':'  ','x':0,'y':0,},
   284:{'num':0,'display':'  ','x':0,'y':0,},
   285:{'num':0,'display':'  ','x':0,'y':0,},
   286:{'num':0,'display':'  ','x':0,'y':0,},
   287:{'num':0,'display':'  ','x':0,'y':0,},
   288:{'num':0,'display':'  ','x':0,'y':0,},
   289:{'num':0,'display':'  ','x':0,'y':0,},
   290:{'num':0,'display':'  ','x':0,'y':0,},
   291:{'num':0,'display':'  ','x':0,'y':0,},
   292:{'num':0,'display':'  ','x':0,'y':0,},
   293:{'num':0,'display':'  ','x':0,'y':0,},
   294:{'num':0,'display':'  ','x':0,'y':0,},
   295:{'num':0,'display':'  ','x':0,'y':0,},
   296:{'num':0,'display':'  ','x':0,'y':0,},
   297:{'num':0,'display':'  ','x':0,'y':0,},
   298:{'num':0,'display':'  ','x':0,'y':0,},
   299:{'num':0,'display':'  ','x':0,'y':0,},
   300:{'num':0,'display':'  ','x':0,'y':0,},
   301:{'num':0,'display':'  ','x':0,'y':0,},
   302:{'num':0,'display':'  ','x':0,'y':0,},
   303:{'num':0,'display':'  ','x':0,'y':0,},
   304:{'num':0,'display':'  ','x':0,'y':0,},
   305:{'num':0,'display':'  ','x':0,'y':0,},
   306:{'num':0,'display':'  ','x':0,'y':0,},
   307:{'num':0,'display':'  ','x':0,'y':0,},
   308:{'num':0,'display':'  ','x':0,'y':0,},
   309:{'num':0,'display':'  ','x':0,'y':0,},
   310:{'num':0,'display':'  ','x':0,'y':0,},
   311:{'num':0,'display':'  ','x':0,'y':0,},
   312:{'num':0,'display':'  ','x':0,'y':0,},
   313:{'num':0,'display':'  ','x':0,'y':0,},
   314:{'num':0,'display':'  ','x':0,'y':0,},
   315:{'num':0,'display':'  ','x':0,'y':0,},
   316:{'num':0,'display':'  ','x':0,'y':0,},
   317:{'num':0,'display':'  ','x':0,'y':0,},
   318:{'num':0,'display':'  ','x':0,'y':0,},
   319:{'num':0,'display':'  ','x':0,'y':0,},
   320:{'num':0,'display':'  ','x':0,'y':0,},
   321:{'num':0,'display':'  ','x':0,'y':0,},
   322:{'num':0,'display':'  ','x':0,'y':0,},
   323:{'num':0,'display':'  ','x':0,'y':0,},
   324:{'num':0,'display':'  ','x':0,'y':0,},
   325:{'num':0,'display':'  ','x':0,'y':0,},
   326:{'num':0,'display':'  ','x':0,'y':0,},
   327:{'num':0,'display':'  ','x':0,'y':0,},
   328:{'num':0,'display':'  ','x':0,'y':0,},
   329:{'num':0,'display':'  ','x':0,'y':0,},
   330:{'num':0,'display':'  ','x':0,'y':0,},
   331:{'num':0,'display':'  ','x':0,'y':0,},
   332:{'num':0,'display':'  ','x':0,'y':0,},
   333:{'num':0,'display':'  ','x':0,'y':0,},
   334:{'num':0,'display':'  ','x':0,'y':0,},
   335:{'num':0,'display':'  ','x':0,'y':0,},
   336:{'num':0,'display':'  ','x':0,'y':0,},
   337:{'num':0,'display':'  ','x':0,'y':0,},
   338:{'num':0,'display':'  ','x':0,'y':0,},
   339:{'num':0,'display':'  ','x':0,'y':0,},
   340:{'num':0,'display':'  ','x':0,'y':0,},
   341:{'num':0,'display':'  ','x':0,'y':0,},
   342:{'num':0,'display':'  ','x':0,'y':0,},
   343:{'num':0,'display':'  ','x':0,'y':0,},
   344:{'num':0,'display':'  ','x':0,'y':0,},
   345:{'num':0,'display':'  ','x':0,'y':0,},
   346:{'num':0,'display':'  ','x':0,'y':0,},
   347:{'num':0,'display':'  ','x':0,'y':0,},
   348:{'num':0,'display':'  ','x':0,'y':0,},
   349:{'num':0,'display':'  ','x':0,'y':0,},
   350:{'num':0,'display':'  ','x':0,'y':0,},
   351:{'num':0,'display':'  ','x':0,'y':0,},
   352:{'num':0,'display':'  ','x':0,'y':0,},
   353:{'num':0,'display':'  ','x':0,'y':0,},
   354:{'num':0,'display':'  ','x':0,'y':0,},
   355:{'num':0,'display':'  ','x':0,'y':0,},
   356:{'num':0,'display':'  ','x':0,'y':0,},
   357:{'num':0,'display':'  ','x':0,'y':0,},
   358:{'num':0,'display':'  ','x':0,'y':0,},
   359:{'num':0,'display':'  ','x':0,'y':0,},
   360:{'num':0,'display':'  ','x':0,'y':0,},
   361:{'num':0,'display':'  ','x':0,'y':0,},
   362:{'num':0,'display':'  ','x':0,'y':0,},
   363:{'num':0,'display':'  ','x':0,'y':0,},
   364:{'num':0,'display':'  ','x':0,'y':0,},
   365:{'num':0,'display':'  ','x':0,'y':0,},
   366:{'num':0,'display':'  ','x':0,'y':0,},
   367:{'num':0,'display':'  ','x':0,'y':0,},
   368:{'num':0,'display':'  ','x':0,'y':0,},
   369:{'num':0,'display':'  ','x':0,'y':0,},
   370:{'num':0,'display':'  ','x':0,'y':0,},
   371:{'num':0,'display':'  ','x':0,'y':0,},
   372:{'num':0,'display':'  ','x':0,'y':0,},
   373:{'num':0,'display':'  ','x':0,'y':0,},
   374:{'num':0,'display':'  ','x':0,'y':0,},
   375:{'num':0,'display':'  ','x':0,'y':0,},
   376:{'num':0,'display':'  ','x':0,'y':0,},
   377:{'num':0,'display':'  ','x':0,'y':0,},
   378:{'num':0,'display':'  ','x':0,'y':0,},
   379:{'num':0,'display':'  ','x':0,'y':0,},
   380:{'num':0,'display':'  ','x':0,'y':0,},
   381:{'num':0,'display':'  ','x':0,'y':0,},
   382:{'num':0,'display':'  ','x':0,'y':0,},
   383:{'num':0,'display':'  ','x':0,'y':0,},
   384:{'num':0,'display':'  ','x':0,'y':0,},
   385:{'num':0,'display':'  ','x':0,'y':0,},
   386:{'num':0,'display':'  ','x':0,'y':0,},
   387:{'num':0,'display':'  ','x':0,'y':0,},
   388:{'num':0,'display':'  ','x':0,'y':0,},
   389:{'num':0,'display':'  ','x':0,'y':0,},
   390:{'num':0,'display':'  ','x':0,'y':0,},
   391:{'num':0,'display':'  ','x':0,'y':0,},
   392:{'num':0,'display':'  ','x':0,'y':0,},
   393:{'num':0,'display':'  ','x':0,'y':0,},
   394:{'num':0,'display':'  ','x':0,'y':0,},
   395:{'num':0,'display':'  ','x':0,'y':0,},
   396:{'num':0,'display':'  ','x':0,'y':0,},
   397:{'num':0,'display':'  ','x':0,'y':0,},
   398:{'num':0,'display':'  ','x':0,'y':0,},
   399:{'num':0,'display':'  ','x':0,'y':0,}}

 

#made an oopsie, cba to correct manually so script
z = 0
n = 0
for x in screen:
  if z == 20:
    z = 0
    n += 1
  screen[x]['num'] = x
  screen[x]['x'] = z
  screen[x]['y'] = n
  z += 1





class E:
  def __init__(self,FType,ERoom,H,damage,defense,down,ETile,name,Ex,Ey,XP,ESpeed):
    self.FType = FType
    self.ERoom = ERoom
    self.H = H
    self.damage = damage
    self.defense = defense
    self.down= down
    self.ETile = ETile
    self.name = name
    self.Ex = Ex
    self.Ey = Ey
    self.XP = XP
    self.ESpeed = ESpeed


Enemy0A = E(2,r5,50,10,5,0,110,'the Brute',1,1,10,3)
Enemy0B = E(2,r5,50,10,5,0,130,'the Brute',1,1,10,3)
Enemy1 = E(1,r24,90,20,10,0,150,'the Gravedigger',1,1,30,2)
Enemy2 = E(1,r35,80,15,10,0,150,'the Ash Wisp',1,1,20,5)
Enemy3 = E(1,r29,80,15,10,0,150,'the Ash Wisp',1,1,20,5)
Enemy4 = E(1,r46,100,30,40,0,150,'the Scorched Knight',1,1,50,3)
Enemy5 = E(1,r50,100,25,35,0,150,'the Guard',1,1,35,5)
Enemy6 = E(1,r55,100,25,35,0,150,'the Guard',1,1,35,5)
Sen1 =   E(1,r52,150,50,50,0,150,'Company Executive Khaan',1,1,100,4)
Enemy7 = E(1,r57,70,35,20,0,150,'the Spiderling',1,1,35,8)
Enemy8 = E(1,r59,70,35,20,0,150,'the Spiderling',1,1,35,8)
Sen2 =   E(1,r60,120,70,30,0,150,'King Arachnid',1,1,100,4)


def bigmapOne():
  print('                                            #:::::::::::::::::#                                            #::::::::::::::::::::::::#                 ')
  print('                                            #                 #          #:::::::::::::::::::::#           #                        #                 ')
  print('                                            #                 #          #                     #           #       #::::::::::::::::#                 ')
  print('                                            #                 #          #                     #           #       #      #:::::::::::::::::::::#     ')
  print('                      #:::::::::::#         #                 #          #:::::::::::::::::::::#           #       #      #                     #     ')
  print('                      #           #---------#                 #                      :                     #       #      #                     #    #:::#')
  print('                      #           #         #                 #                #:::::::::::::::::::::#     #:::::::#      #                     #--- #   #<--CRIMSON')
  print('     #::::::::::#     #           #         #:::::::::::::::::#                #                     #         :          #                     #    #   #   MINES')
  print('     #          #-----#           #                      :                     #                     #     #::::::::#     #                     #    #:::#')
  print('     #          #     #           #             #::::::::::::::::::#           #                     #     #        #     #                     #    ')
  print('     #          #     #:::::::::::#             #                  #           #                     #-----#        #     #:::::::::::::::::::::#    ')
  print('     #          #            :                  #                  #           #       stairs        #     #        #                           ')
  print('     #          #       #::::::::::#            #                  #-----------#                     #     #::::::::#                                 ')
  print('     #          #       #          #            #                  #           #                     #                     #::::::::#                 ')
  print('     #::::::::::#       #          #            #                  #           #                     #     #::::::::::#    #        #                 ')
  print('           :            #          #            #                  #           #                     #     #          #    #        #                 ')
  print('           :            #          #            #                  #           #                     #     #          #----#        #                 ')
  print('#::::::::::::::::#      #          #            #::::::::::::::::::#           #:::::::::::::::::::::#     #::::::::::#    #::::::::#                 ')
  print('#                #      #          #                      :                                                                     :                     ')
  print('#                #      #          #                      :                                                              #::::::::::#                 ')
  print('#                #      #          #         #::::::::::::::::::::::::::#                                                #          #                 ')
  print('#                #      #          #         #                          #            #:::::::#        #:::::::::::::#    #          #                 ')
  print('#                #      #          #         #                          #            #       #        #             #    #          #                 ')
  print('#                #      #          #         #                          #------------#       #--------#             #    #::::::::::#                 ')
  print('#                #      #          #         #@@@@@@@@@@@               #            #:::::::#        #             #                             ')
  print('#::::::::::::::::#      #          #         #@@@@@@@@@@@@@@@           #                :            #:::::::::::::#                             ')
  print('              :         #          #         #            @@@@@@@@@@    #                :                      :                                 ')
  print('           #::::::#     #          #         #                 @@@@@@@@@#                :                  :::::::::                            ')
  print('           #      #-----#          #         #       river          @@@@#              #:::::::::::::#      #       #                           ')
  print('           #      #     #          #---------#                          #              #             #      #       #                           ')
  print('           #      #     #          #         #                          #              #             #      #       #                          ')
  print('           #::::::#     #::::::::::#         #::::::::::::::::::::::::::#              #:::::::::::::#      :::::::::                             ')
  print('                              :                          :                                                      :                                 ')
  print('                              :                 #::::::::::::::::#                                              :                                 ')
  print('                              :                 #        /       #                                              :                                 ')
  print('                         #::::::::#             #       /        #                                              :                                 ')
  print('                         #        #             #      /         #                                              :                                 ')
  print('                         #  map   #             #     /          #                                           #::::::#                           ')
  print('                         #        #------------=#    |           #      #:::::::#                            #      #                           ')
  print('                         #        #             #    |  ravine   #      #       #                            #      #                           ')
  print('                         #        #             #   /            #      #       #:---------------------------#      #                           ')
  print('                         #        #             #  /             #::::::#       #                            #::::::#                           ')
  print('                         #::::::::#             # /              #      #       #                                                                 ')
  print('                                                #::::::::::::::::#      #:::::::#                                                                 ')
  print('                                                                            :                                                                    ')
  print('                                                                         #:::::::#                                                                 ')
  print('                                                                         #       #                                                                ')
  print('                                                                         #       # <--Door                                                           ')
  print('                                                                         #       #                                                                ')
  print('                                                                         #       #                                                                ')
  print('                                                                         #:::::::#                                                                ')
  


def bigmapTwoOne():
  print("                                                                                                                                                   #::::::::::::::::::#                                       ")
  print("                                                                                                                                  #::::::#         #                  #                                       ")  
  print("                                                                                                                                  #      #---------#                  #                                    ")
  print("                                                                                                                                  #      #         #                  #    #:::::::#                         ")   
  print("                                                                                                                                  #::::::#         #                  #    #       #                         ")   
  print("                                  #::::::::::::::::#                                                                                 :             #                  #----#       #=======                  ") 
  print("                                  #                #      #:::::::#                                                       #:::::::::::::::::::::#  #                  #    #       #                        ")    
  print("                                  #                #      #       #                                                       #                     #  #                  #    #:::::::#                        ")    
  print("                                  #                #------#       #                                           #:::::::#   #                     #  #                  #                                    ")     
  print("                                  #    MINE HOUSE  #      #:::::::#                               #::::::#    #       #   #        SPIDER       #  #::::::::::::::::::#                                    ")     
  print("                                  #                #          :                                   #      #----#       #---#          CAVES      #     #::::::#                                             ")     
  print("                                  #                #          :                                   #      #    #       #   #                     #     #      #                                            ")      
  print("                                  #                #    #:::::::::::#     #:::::::#               #      #    #:::::::#   #                     #-----#      #                                            ")    
  print("                                  #                #    #           #     #       #               #::::::#                #:::::::::::::::::::::#     #::::::#                                            ")      
  print("                                  #::::::::::::::::#    #           #-----#       #                                                   :                                                                  ") 
  print("                                     :       #::::#     #           #     #       #                                                   :                                                                   ")      
  print("                                     :       #    #-----#           #     #:::::::#     #:::::::::::::::::::::::::::::::::::::#    #:::::#                                                               ")       
  print("                                     :       #    #     #           #         :         #                                     #    #     #                                                              ")        
  print("                                 #:::::::#   #    #     #           #    #::::::::#     #                                     #----#     #                                                              ")        
  print("                                 #       #   #::::#     #:::::::::::#    #        #-----#               TILES                 #    #:::::#                                                             ")        
  print("                                 #       #                :              #        #     #                                     #       :               #::::::::#                                       ")         
  print("                                 #       #           #::::::#            #        #     #:::::::::::::::::::::::::::::::::::::#       :               #        #                                        ")        
  print("                                 #       #           #      #            #::::::::#                                                   :               #        #                                        ")        
  print("                                 #:::::::#           #      #                :                                                        :               #        #                                       ")         
  print("                                    :                #::::::# <-- Map        :                                              #::::::::::::::::::::#    #        #                                       ")         
  print("                        #::::::::::::::#               :                     :                                              #                  ..#    #        #                                       ")         
  print("                        #              #      #:::::::::::#                  :                                              #                    #    #        #                                       ")         
  print("                        #              #      #           #      #::::::::::::::::::::::::#                       #::::::#  #                    #    #        #                                       ")         
  print("     exit--> #:::::::#  #              #      #           #      #                        #                       #      #  #                    #    #        #                                       ")         
  print("             #       #  #              #      #           #::::::#                        #    #::::::::::#       #      #--#        LOCK        #----#        #                                       ")         
  print("         ====#       #--#              #      #           #      #                        #    #          #       #      #  #       HOUSE        #    #        #                                      ")          
  print("             #       #  #              #      #           #      #                        #    #          #       #      #  #                    #    #        #                                      ")          
  print("             #:::::::#  #              #      #:::::::::::#      #        STACKS          #----#          #       #      #  #                    #    #        #                                      ")          
  print("                        #              #         :               #                        #    #          #       #::::::#  #                    #    #        #                                     ")           
  print("                        #::::::::::::::#         :               #                        #    #          #                 #::::::::::::::::::::#    #        #                                         ")       
  print("                                :                :               #                        #    #::::::::::#                            :              #        #                                                ")
  print("                                :           #::::::::#           #                        #                                            :              #::::::::#                                                ")
  print("                            #:::::::#       #        #           #                        #                                            :                                                               ")
  print("                            #       #-------#        #           #                        #                           #:::::::#        :                                                                        ")
  print("                            #       #       #        #           #::::::::::::::::::::::::#                           #       #    #:::::::::#                                                                  ")
  print("                            #:::::::#       #::::::::#                                :                               #       #    #         #            #:::::::::#       #::::::::::#                       ") 
  print("             #::::::::::#       :                                                     :                               #       #----#         #            #         #       #          #                     ")  
  print("             #          #       :                                                     :                               #       #    #         #            #         #-------#          #============         ")     
  print("             #          #       :     #:::::::::::::::::::::::::::::::::::#       #:::::::#                           #:::::::#    #:::::::::#            #         #       #          #                     ")
  print("             #          #   #::::::#  #                                   #       #       #                               :                               #:::::::::#       #          #                     ")   
  print("             #          #---#      #--#            CHAINS                 #-------#       #                               :                                   :             #::::::::::#                    ")    
  print("             #          #   #      #  #                                   #       #       #                               :                                   :                                          ")       
  print("             #          #   #::::::#  #                                   #       #       #                           #:::::::::::::::::#          #:::::::::::::::::::::#                              ")        
  print("             #          #             #:::::::::::::::::::::::::::::::::::#       #:::::::#                           #                 #          #                     #                              ")        
  print("             #::::::::::#                                                                                             #                 #          #                     #                               ")       
  print("                                                                                                                      #                 #          #                     #                              ")        
  print("                                                                                                                      #                 #----------#                     #                             ")         
  print("                                                                                                                      #                 #          #      COURTYARD      #                             ")         
  print("                                                                                                                      #                 #          #                     #                            ")          
  print("                                                                                                                      #                 #          #                     #                            ")          
  print("                                                                                                                      #                 #          #                     #                            ")          
  print("                                                                                                                      #:::::::::::::::::#          #                     #                            ")          
  print("                                                                                                                                                   #:::::::::::::::::::::#         ")




def ice_caves():
  
  print(""+Fore.RESET+"     "+rooms[r13]['mmc']+"---    "+rooms[r14]['mmc']+"---                              ")
  print("    "+rooms[r13]['mmc']+"|   |"+Fore.RESET+"--"+rooms[r14]['mmc']+"|   |"+Fore.RESET+" ...              ")
  print("     "+rooms[r13]['mmc']+"---    "+rooms[r14]['mmc']+"- - "+Fore.RESET+"                    ")
  print("      |     "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"                 ")
  print("      |     "+rooms[r10]['mmc']+"[ ]                 ")
  print("     "+rooms[r12]['mmc']+"----   "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"       :              ")
  print("    "+rooms[r12]['mmc']+"|    |  "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"       :              ")
  print("     "+rooms[r12]['mmc']+"----   "+rooms[r10]['mmc']+"[ ]   "+rooms[r5]['mmc']+"----------"+Fore.RESET+"              ")
  print("       |    "+rooms[r10]['mmc']+"[ ]   "+rooms[r5]['mmc']+"|        |"+Fore.RESET+"---"+rooms[r6]['mmc']+"[ ]"+Fore.RESET+"--"+rooms[r7]['mmc']+"[___]              ")
  print("      "+rooms[r11]['mmc']+"[ ]"+Fore.RESET+"---"+rooms[r10]['mmc']+"[ ]   "+rooms[r5]['mmc']+"|        |"+Fore.RESET+"    |     |              ")
  print("            "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"---"+rooms[r5]['mmc']+"|        |  "+rooms[r9]['mmc']+"[___]  "+rooms[r8]['mmc']+"[ ]"+Fore.RESET+"              ")
  print("             |    "+rooms[r5]['mmc']+"---------- "+Fore.RESET+"         |              ")
  print("             |        |               |              ")
  print("             |      "+rooms[r2]['mmc']+"----- "+Fore.RESET+"            |              ")
  print("            "+rooms[r4]['mmc']+"[  ]"+Fore.RESET+"----"+rooms[r2]['mmc']+"|   |"+Fore.RESET+"---"+rooms[r1]['mmc']+"[ ]"+Fore.RESET+"------"+rooms[r3]['mmc']+"[ ]              ")
  print("            "+rooms[r4]['mmc']+"[  ]    "+rooms[r2]['mmc']+"|   |"+Fore.RESET+"    |              ")
  print("                    "+rooms[r2]['mmc']+"-----   "+rooms[r0]['mmc']+"[ ]<--- Start              ")
  

def crypts():
  print(""+Fore.RESET+"       "+rooms[r15]['mmc']+" -----    "+rooms[r18]['mmc']+" ----------  "+rooms[r20]['mmc']+" ----------                   ")
  print("       "+rooms[r15]['mmc']+"|     |   "+rooms[r18]['mmc']+"|          | "+rooms[r20]['mmc']+"|          |"+Fore.RESET+"----+                 ")      
  print("    ..."+rooms[r15]['mmc']+"|     |    "+rooms[r18]['mmc']+"----------   "+rooms[r20]['mmc']+"----------"+Fore.RESET+"     |                 ")
  print("        "+rooms[r15]['mmc']+"-----"+Fore.RESET+"            |      |    "+rooms[r24]['mmc']+"-------------------- "+Fore.RESET+"                ")
  print("          |       "+rooms[r17]['mmc']+"---------"+Fore.RESET+"     |   "+rooms[r24]['mmc']+"|                    |"+Fore.RESET+"--"+rooms[r25]['mmc']+"[ ]                 ")
  print("       "+rooms[r16]['mmc']+" -----    "+rooms[r17]['mmc']+"|         |"+Fore.RESET+"    |   "+rooms[r24]['mmc']+"|                    |                 ")
  print("       "+rooms[r16]['mmc']+"|     |"+Fore.RESET+"---"+rooms[r17]['mmc']+"|         |"+Fore.RESET+"---"+rooms[r19]['mmc']+"[ ]   "+rooms[r24]['mmc']+"--------------------                 ")
  print("       "+rooms[r16]['mmc']+"|     |   "+rooms[r17]['mmc']+"|         |"+Fore.RESET+"    |     |                 ")
  print("        "+rooms[r16]['mmc']+"-----     "+rooms[r17]['mmc']+"---------    "+rooms[r21]['mmc']+"[ ]"+Fore.RESET+"--"+rooms[r23]['mmc']+"[   ]"+Fore.RESET+"                 ")
  print("          :                           |                 ")
  print("          :                         "+rooms[r22]['mmc']+" ---                 ")
  print("                                    "+rooms[r22]['mmc']+"|   |                 ")
  print("                                     "+rooms[r22]['mmc']+"---                 ")


def wastes():
  print(""+Fore.RESET+"                              ...."+rooms[r39]['mmc']+"[ ] "+Fore.RESET+"             ")
  print("                                   |               ")
  print("          :                       "+rooms[r38]['mmc']+"-- "+Fore.RESET+"              ")
  print("          :         :            "+rooms[r38]['mmc']+"|  | "+Fore.RESET+"             ")
  print("        "+rooms[r31]['mmc']+" -- "+Fore.RESET+"        :      "+rooms[r34]['mmc']+"---   "+rooms[r38]['mmc']+"|  |"+Fore.RESET+"              ")
  print("  "+rooms[r30]['mmc']+"[ ]"+Fore.RESET+"---"+rooms[r31]['mmc']+"|  |"+Fore.RESET+"--"+rooms[r32]['mmc']+"[ ]"+Fore.RESET+"--"+rooms[r33]['mmc']+"[ ]"+Fore.RESET+"----"+rooms[r34]['mmc']+"|   |  "+rooms[r38]['mmc']+"|  | "+Fore.RESET+"             ")
  print("   |     "+rooms[r31]['mmc']+"--                "+rooms[r34]['mmc']+"---   "+rooms[r38]['mmc']+"|  |"+Fore.RESET+"              ")
  print("   |      |                 |    "+rooms[r38]['mmc']+" --"+Fore.RESET+"               ")
  print(""+rooms[r29]['mmc']+" ------  "+rooms[r40]['mmc']+"[  ]    "+rooms[r27]['mmc']+"----"+Fore.RESET+"       |     |                ")
  print(""+rooms[r29]['mmc']+"|      |        "+rooms[r27]['mmc']+"|    |"+Fore.RESET+"-----"+rooms[r35]['mmc']+"[ ]"+Fore.RESET+"---"+rooms[r36]['mmc']+"[ ]               ")
  print(""+rooms[r29]['mmc']+"|      |"+Fore.RESET+"---"+rooms[r28]['mmc']+"[ ]"+Fore.RESET+"--"+rooms[r27]['mmc']+"|    |"+Fore.RESET+"            |                ")
  print(""+rooms[r29]['mmc']+"|      |        "+rooms[r27]['mmc']+" ----          "+rooms[r37]['mmc']+" -----              ")
  print(" "+rooms[r29]['mmc']+"------ "+Fore.RESET+"          |            "+rooms[r37]['mmc']+"|     |             ")
  print("                 "+rooms[r26]['mmc']+"[ ]<--start   "+rooms[r37]['mmc']+" -----              ")


def deltas():
  print(""+Fore.RESET+"          ...."+rooms[r46]['mmc']+"[ ]"+Fore.RESET+"....                        ")
  print("               |                     ")
  print("             "+rooms[r44]['mmc']+" ---                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |             "+rooms[r45]['mmc']+"[ ]                  ")
  print("             "+rooms[r44]['mmc']+"|   |"+Fore.RESET+"              |                  ")
  print("             "+rooms[r44]['mmc']+" --- "+Fore.RESET+"        "+rooms[r41]['mmc']+"------------"+Fore.RESET+"                  ")
  print("               |         "+rooms[r41]['mmc']+"|            |                  ")
  print("            "+rooms[r42]['mmc']+"------       "+rooms[r41]['mmc']+"|            |                  ")
  print("    "+rooms[r43]['mmc']+" --    "+rooms[r42]['mmc']+"|      |      "+rooms[r41]['mmc']+"|            |                  ")
  print("    "+rooms[r43]['mmc']+"|  |"+Fore.RESET+"---"+rooms[r42]['mmc']+"|      |"+Fore.RESET+"------"+rooms[r41]['mmc']+"|            | "+Fore.RESET+".....            ")
  print("     "+rooms[r43]['mmc']+"--    "+rooms[r42]['mmc']+" ------       "+rooms[r41]['mmc']+"|            | "+Fore.RESET+"                 ")
  print("     :                   "+rooms[r41]['mmc']+" ------------ "+Fore.RESET+"                 ")
  print("     :                         :                  ")
  print("     :                         :                  ")


def lockhouse():
  print(''+Fore.RESET+'                       :       ')
  print('                       :     ')
  print('                      '+rooms[r54]['mmc']+'[ ]     ')
  print('    '+rooms[r55]['mmc']+'------------ '+Fore.RESET+'      |    '+rooms[r52]['mmc']+'-------     ')
  print('   '+rooms[r55]['mmc']+'|            |     '+rooms[r53]['mmc']+'[ ]'+Fore.RESET+'--'+rooms[r52]['mmc']+'|       |'+Fore.RESET+'     ')
  print('    '+rooms[r55]['mmc']+'------------           '+rooms[r52]['mmc']+'|       | '+Fore.RESET+'     ')
  print('        |                   '+rooms[r52]['mmc']+'-------'+Fore.RESET+'     ')
  print('      '+rooms[r47]['mmc']+'--------'+Fore.RESET+'                |     ')
  print('     '+rooms[r47]['mmc']+'|        |'+Fore.RESET+'               |     ')
  print(' ....'+rooms[r47]['mmc']+'|        |'+Fore.RESET+'----'+rooms[r50]['mmc']+'[ ]      '+rooms[r51]['mmc']+'-----     ')
  print('     '+rooms[r47]['mmc']+'|        |'+Fore.RESET+'     |      '+rooms[r51]['mmc']+'|     |     ')
  print('     '+rooms[r47]['mmc']+' --------'+Fore.RESET+'     '+rooms[r49]['mmc']+'[ ]'+Fore.RESET+'-----'+rooms[r51]['mmc']+'|     |'+Fore.RESET+'     ')
  print('          |                 '+rooms[r51]['mmc']+'-----'+Fore.RESET+'     ')
  print('        '+rooms[r48]['mmc']+'[   ]     ')


def spiders():
   print(''+Fore.RESET+'     :          ')
   print('     :          ')
   print('    '+rooms[r62]['mmc']+'---          ')
   print('   '+rooms[r62]['mmc']+'|   |          ')
   print('    '+rooms[r62]['mmc']+'---'+Fore.RESET+'          ')
   print('     |          ')
   print('   '+rooms[r60]['mmc']+'-----     '+rooms[r59]['mmc']+'---          ')
   print('  '+rooms[r60]['mmc']+'|     |'+Fore.RESET+'---'+rooms[r59]['mmc']+'|   |          ')
   print('  '+rooms[r60]['mmc']+'|     |    '+rooms[r59]['mmc']+'---          ')
   print('   '+rooms[r60]['mmc']+'-----'+Fore.RESET+'      |          ')
   print('     |      '+rooms[r56]['mmc']+'--------          ')
   print('    '+rooms[r61]['mmc']+'---    '+rooms[r56]['mmc']+'|        |          ')
   print('   '+rooms[r61]['mmc']+'|   |'+Fore.RESET+'---'+rooms[r56]['mmc']+'|        |'+Fore.RESET+'....          ')
   print('    '+rooms[r61]['mmc']+'---    '+rooms[r56]['mmc']+'|        |          ')
   print('            '+rooms[r56]['mmc']+'--------'+Fore.RESET+'          ')
   print('               |           ')
   print('              '+rooms[r57]['mmc']+'[ ]'+Fore.RESET+'          ')
   print('               |          ')
   print('             '+rooms[r58]['mmc']+'[   ]          ')


def shrooms():
  print(''+Fore.RESET+'               '+rooms[r70]['mmc']+'[ ]                                ')
  print('      '+rooms[r71]['mmc']+'-----     '+Fore.RESET+'|                                         ')
  print('     '+rooms[r71]['mmc']+'|     |   '+rooms[r69]['mmc']+'---                                       ')
  print('     '+rooms[r71]['mmc']+'|     |'+Fore.RESET+'--'+rooms[r69]['mmc']+'|   |        '+rooms[r72]['mmc']+'---                               ')
  print('      '+rooms[r71]['mmc']+'-----    '+rooms[r69]['mmc']+'---        '+rooms[r72]['mmc']+'|   |'+Fore.RESET+'...                    ')
  print('                '+Fore.RESET+'|          '+rooms[r72]['mmc']+'---                                            ')
  print('            '+rooms[r66]['mmc']+'----------      '+Fore.RESET+'|                                             ')
  print('           '+rooms[r66]['mmc']+'|          |    '+rooms[r67]['mmc']+'---                                               ')
  print('           '+rooms[r66]['mmc']+'|          |'+Fore.RESET+'---'+rooms[r67]['mmc']+'|   |'+Fore.RESET+'--'+rooms[r68]['mmc']+'[ ]                                ')
  print('           '+rooms[r66]['mmc']+'|          |    '+rooms[r67]['mmc']+'---                                             ')
  print('           '+rooms[r66]['mmc']+'|          |                                                   ')
  print('            '+rooms[r66]['mmc']+'----------                                             ')
  print('                |                                                 ')
  print('       '+rooms[r63]['mmc']+'---     '+rooms[r64]['mmc']+'---     '+rooms[r65]['mmc']+'---                                           ')
  print('      '+rooms[r63]['mmc']+'|   |'+Fore.RESET+'---'+rooms[r64]['mmc']+'|   |'+Fore.RESET+'---'+rooms[r65]['mmc']+'|   |                                  ')
  print('       '+rooms[r63]['mmc']+'---     '+rooms[r64]['mmc']+'---     '+rooms[r65]['mmc']+'---                          ')
  print('        '+Fore.RESET+':                                                             ')
  print('        :                                        ')


def caves():
  print('             '+rooms[r82]['mmc']+'---               ')
  print('            '+rooms[r82]['mmc']+'|   |'+Fore.RESET+'---'+rooms[r83]['mmc']+'[ ]                ')
  print('             '+rooms[r82]['mmc']+'---     '+Fore.RESET+'|        ')
  print('              '+Fore.RESET+'|     '+rooms[r84]['mmc']+'---      ')
  print('             '+rooms[r81]['mmc']+'---   '+rooms[r84]['mmc']+'|   |       ')
  print('         '+Fore.RESET+'...'+rooms[r81]['mmc']+'|   |   '+rooms[r84]['mmc']+'---      ')
  print('             '+rooms[r81]['mmc']+'---            ')
  print('              '+Fore.RESET+'|                   ')
  print('             '+rooms[r80]['mmc']+'---                ')
  print('            '+rooms[r80]['mmc']+'|   |            ')
  print('            '+rooms[r80]['mmc']+'|   |          ')
  print('            '+rooms[r80]['mmc']+'|   |           ')
  print('            '+rooms[r80]['mmc']+'|   |            ')
  print('     '+rooms[r77]['mmc']+'[ ]'+Fore.RESET+'----'+rooms[r80]['mmc']+'|   |              ')
  print('      '+Fore.RESET+'|      '+rooms[r80]['mmc']+'---               ')
  print('      '+Fore.RESET+'|       '+Fore.RESET+'|                ')
  print('   '+rooms[r76]['mmc']+'-----     '+rooms[r78]['mmc']+'---                ')
  print('  '+rooms[r76]['mmc']+'|     |'+Fore.RESET+'---'+rooms[r78]['mmc']+'|   |'+Fore.RESET+'---'+rooms[r79]['mmc']+'[ ]             ')
  print('  '+rooms[r76]['mmc']+'|     |    '+rooms[r78]['mmc']+'---                  ')
  print('   '+rooms[r76]['mmc']+'-----                         ')
  print('     '+Fore.RESET+':                               ')
  print('     :                     ')


def mists():
  print(''+Fore.RESET+'       :                                    ')
  print('       :                                    ')
  print('     '+rooms[r86]['mmc']+'-----   '+rooms[r89]['mmc']+'[ ]                                    ')
  print(' '+Fore.RESET+'...'+rooms[r86]['mmc']+'|     |   '+Fore.RESET+'|    '+rooms[r88]['mmc']+'---                          ')
  print('    '+rooms[r86]['mmc']+'|     |'+Fore.RESET+'--'+rooms[r87]['mmc']+'[ ]'+Fore.RESET+'--'+rooms[r88]['mmc']+'|   |                                ')
  print('     '+rooms[r86]['mmc']+'-----         '+rooms[r88]['mmc']+'---                        ')
  print('      '+Fore.RESET+'|             |                       ')
  print('   '+rooms[r85]['mmc']+'-----    '+rooms[r75]['mmc']+'-----------------             ')
  print('  '+rooms[r85]['mmc']+'|     |  '+rooms[r75]['mmc']+'|                 |               ')
  print('  '+rooms[r85]['mmc']+'|     |'+Fore.RESET+'--'+rooms[r75]['mmc']+'|                 |               ')
  print('   '+rooms[r85]['mmc']+'-----   '+rooms[r75]['mmc']+'|                 |               ')
  print('           '+rooms[r75]['mmc']+'|                 |'+Fore.RESET+'....          ')
  print('           '+rooms[r75]['mmc']+'|                 |               ')
  print('           '+rooms[r75]['mmc']+'|                 |               ')
  print('           '+rooms[r75]['mmc']+'|                 |               ')
  print('            '+rooms[r75]['mmc']+'-----------------               ')
  print('              '+rooms[r73]['mmc']+'---    '+Fore.RESET+'|                       ')
  print('          '+Fore.RESET+'...'+rooms[r73]['mmc']+'|   |'+Fore.RESET+'--'+rooms[r74]['mmc']+'[ ]                       ')
  print('              '+rooms[r73]['mmc']+'---                           ')
  print('                                            ')


def parlour():
  print(''+Fore.RESET+'        '+rooms[r90]['mmc']+'--------       ')
  print('       '+rooms[r90]['mmc']+'|        |      ')
  print('       '+rooms[r90]['mmc']+'|        |'+Fore.RESET+'....  ')
  print('       '+rooms[r90]['mmc']+'|        |      ')
  print('        '+rooms[r90]['mmc']+'--------       ')
  print('            '+Fore.RESET+'|          ')
  print('           '+rooms[r91]['mmc']+'---         ')
  print('          '+rooms[r91]['mmc']+'|   |         ')
  print('          '+rooms[r91]['mmc']+'|   |        ')
  print('          '+rooms[r91]['mmc']+'|   |        ')
  print('           '+rooms[r91]['mmc']+'---         ')
  print('            '+Fore.RESET+'|          ')
  print('    '+rooms[r93]['mmc']+'---    '+rooms[r92]['mmc']+'---         ')
  print('   '+rooms[r93]['mmc']+'|   |'+Fore.RESET+'--'+rooms[r92]['mmc']+'|   |        ')
  print('    '+rooms[r93]['mmc']+'---    '+rooms[r92]['mmc']+'---         ')


def river():
  print('  '+rooms[r95]['mmc']+'[ ]              ')
  print('   '+Fore.RESET+'|              ')
  print('  '+rooms[r94]['mmc']+'---     '+rooms[r96]['mmc']+'--------------    '+rooms[r97]['mmc']+'---       ')
  print(' '+rooms[r94]['mmc']+'|   |'+Fore.RESET+'---'+rooms[r96]['mmc']+'|              |'+Fore.RESET+'--'+rooms[r97]['mmc']+'|   |        ')
  print('  '+rooms[r94]['mmc']+'---     '+rooms[r96]['mmc']+'--------------    '+rooms[r97]['mmc']+'---          ')
  print('   '+Fore.RESET+':                         |            ')
  print('   '+Fore.RESET+':                   '+rooms[r99]['mmc']+'[ ]'+Fore.RESET+'--'+rooms[r98]['mmc']+'[ ]           ')
  print('                        '+Fore.RESET+'|                  ')
  print('                      '+rooms[r100]['mmc']+'------------         ')
  print('                     '+rooms[r100]['mmc']+'|            |'+Fore.RESET+'--'+rooms[r100tr]['mmc']+'[ ]'+Fore.RESET+'...    ')
  print('                      '+rooms[r100]['mmc']+'------------        ')




room0C = Fore.RESET

rooms = {r0:{'type':r0   ,'left':'blank' ,'right':'blank' ,'up':r1      ,'down':'blank' ,'item':'blank'                ,'inspect':r0d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm},
         r1:{'type':r1   ,'left':r2      ,'right':r3      ,'up':'blank' ,'down':r0      ,'item':'blank'                ,'inspect':r1d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm},
         r2:{'type':r2   ,'left':r4      ,'right':r1      ,'up':r5      ,'down':'blank' ,'item':'Food (Small)'         ,'inspect':r2d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm},
         r3:{'type':r3   ,'left':r1      ,'right':'blank' ,'up':r8      ,'down':'blank' ,'item':'blank'                ,'inspect':r3d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm},
         r4:{'type':r4   ,'left':'blank' ,'right':r2      ,'up':r10     ,'down':'blank' ,'item':'Map (Crypts)'         ,'inspect':r4d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm},
         r5:{'type':r5   ,'left':r10     ,'right':r6      ,'up':r16     ,'down':r2      ,'item':'Food (Small)'         ,'inspect':r5d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': r5BM},
         r6:{'type':r6   ,'left':r5      ,'right':r7      ,'up':'blank' ,'down':r9      ,'item':'blank'                ,'inspect':r6d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm},
         r7:{'type':r7   ,'left':r6      ,'right':'blank' ,'up':'blank' ,'down':r8      ,'item':'Food (Small)'         ,'inspect':r7d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm},
         r8:{'type':r8   ,'left':'blank' ,'right':'blank' ,'up':r7      ,'down':r3      ,'item':'Lantern'              ,'inspect':r8d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm},
         r9:{'type':r9   ,'left':'blank' ,'right':'blank' ,'up':r6      ,'down':'blank' ,'item':'Crown'                ,'inspect':r9d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm},
         r10:{'type':r10 ,'left':r11     ,'right':r5      ,'up':r14     ,'down':r4      ,'item':'blank'                ,'inspect':r10d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm},
         r11:{'type':r11 ,'left':'blank' ,'right':r10     ,'up':r12     ,'down':'blank ','item':'Rusty Sword'          ,'inspect':r11d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm},
         r12:{'type':r12 ,'left':'blank' ,'right':'blank' ,'up':r13     ,'down':r11     ,'item':'Explosive Charge'     ,'inspect':r12d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm},
         r13:{'type':r13 ,'left':'blank' ,'right':r14     ,'up':'blank' ,'down':r12     ,'item':'KEY TO CRIMSON CAVES' ,'inspect':r13d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm},
         r14:{'type':r14 ,'left':r13     ,'right':r15     ,'up':'blank' ,'down':r10     ,'item':'blank'                ,'inspect':r14d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm},
         r15:{'type':r15 ,'left':r14     ,'right':'blank' ,'up':'blank' ,'down':r16     ,'item':'blank'                ,'inspect':r15d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r16:{'type':r16 ,'left':'blank' ,'right':r17     ,'up':r15     ,'down':r5      ,'item':'blank'                ,'inspect':r16d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r17:{'type':r17 ,'left':r16     ,'right':r19     ,'up':r18     ,'down':'blank ','item':'blank'                ,'inspect':r17d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r18:{'type':r18 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r17     ,'item':'Lava Splash (Scroll)' ,'inspect':r18d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r19:{'type':r19 ,'left':r17     ,'right':'blank' ,'up':r20     ,'down':r21     ,'item':'blank'                ,'inspect':r19d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r20:{'type':r20 ,'left':'blank' ,'right':r24     ,'up':'blank' ,'down':r19     ,'item':'blank'                ,'inspect':r20d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r21:{'type':r21 ,'left':'blank' ,'right':r23     ,'up':r19     ,'down':'blank ','item':'blank'                ,'inspect':r21d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r22:{'type':r22 ,'left':'blank' ,'right':'blank' ,'up':r23     ,'down':'blank ','item':'Leather Armour'       ,'inspect':r22d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r23:{'type':r23 ,'left':r21     ,'right':'blank' ,'up':r24     ,'down':r22     ,'item':'blank'                ,'inspect':r23d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r24:{'type':r24 ,'left':'blank' ,'right':r25     ,'up':r20     ,'down':r23     ,'item':'blank'                ,'inspect':r24d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r24BM},
         r25:{'type':r25 ,'left':r24     ,'right':'blank' ,'up':'blank' ,'down':'blank ','item':'blank'                ,'inspect':r25d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r26:{'type':r26 ,'left':'blank' ,'right':'blank' ,'up':r27     ,'down':r25     ,'item':'blank'                ,'inspect':r26d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r27:{'type':r27 ,'left':r28     ,'right':r35     ,'up':'blank' ,'down':r26     ,'item':'blank'                ,'inspect':r27d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r28:{'type':r28 ,'left':r29     ,'right':r27     ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r28d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r29:{'type':r29 ,'left':'blank' ,'right':r28     ,'up':r30     ,'down':'blank' ,'item':'Pickaxe'              ,'inspect':r29d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r29BM},
         r30:{'type':r30 ,'left':'blank' ,'right':r31     ,'up':'blank' ,'down':r29     ,'item':'Food (Medium)'        ,'inspect':r30d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r31:{'type':r31 ,'left':r30     ,'right':r32     ,'up':r43     ,'down':r40     ,'item':'blank'                ,'inspect':r31d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r32:{'type':r32 ,'left':r31     ,'right':r33     ,'up':'blank' ,'down':'blank' ,'item':'Map (Crimson Caves)'  ,'inspect':r32d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'safe','rest':'y' , 'bmap': Nbm},
         r33:{'type':r33 ,'left':r32     ,'right':r34     ,'up':r41     ,'down':'blank' ,'item':'blank'                ,'inspect':r33d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r34:{'type':r34 ,'left':r33     ,'right':'blank' ,'up':'blank' ,'down':r35     ,'item':'blank'                ,'inspect':r34d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r35:{'type':r35 ,'left':r27     ,'right':r36     ,'up':r34     ,'down':'blank' ,'item':'blank'                ,'inspect':r35d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r35BM},
         r36:{'type':r36 ,'left':r35     ,'right':'blank' ,'up':r38     ,'down':r37     ,'item':'Food (Medium)'        ,'inspect':r36d, 'map':'f2','minimap': 'wastes'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r37:{'type':r37 ,'left':'blank' ,'right':'blank' ,'up':r36     ,'down':'blank' ,'item':'Fire Bolt (Scroll)'   ,'inspect':r37d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r38:{'type':r38 ,'left':'blank' ,'right':'blank' ,'up':r39     ,'down':r36     ,'item':'blank'                ,'inspect':r38d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r39:{'type':r39 ,'left':r41     ,'right':'blank' ,'up':'blank' ,'down':r38     ,'item':'Food (Small)'         ,'inspect':r39d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r40:{'type':r40 ,'left':'blank' ,'right':'blank' ,'up':r31     ,'down':'blank' ,'item':'Mining Gear'          ,'inspect':r40d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r41:{'type':r41 ,'left':r42     ,'right':r39     ,'up':r45     ,'down':r33     ,'item':'Crown'                ,'inspect':r41d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r42:{'type':r42 ,'left':r43     ,'right':r41     ,'up':r44     ,'down':'blank' ,'item':'blank'                ,'inspect':r42d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r43:{'type':r43 ,'left':'blank' ,'right':r42     ,'up':'blank' ,'down':r31     ,'item':'Scorched Chainmail'   ,'inspect':r43d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r44:{'type':r44 ,'left':'blank' ,'right':'blank' ,'up':r46     ,'down':r42     ,'item':'blank'                ,'inspect':r44d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r45:{'type':r45 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r41     ,'item':'Crown'                ,'inspect':r45d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r46:{'type':r46 ,'left':r56     ,'right':r47     ,'up':'blank' ,'down':r44     ,'item':'blank'                ,'inspect':r46d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r46BM},
         r47:{'type':r47 ,'left':r46     ,'right':r50     ,'up':r55     ,'down':r48     ,'item':'blank'                ,'inspect':r47d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r48:{'type':r48 ,'left':'blank' ,'right':'blank' ,'up':r47     ,'down':'blank' ,'item':'Steel Sword'          ,'inspect':r48d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r49:{'type':r49 ,'left':'blank' ,'right':r51     ,'up':r50     ,'down':'blank' ,'item':'blank'                ,'inspect':r49d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r50:{'type':r50 ,'left':r47     ,'right':'blank' ,'up':'blank' ,'down':r49     ,'item':'blank'                ,'inspect':r50d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r50BM},
         r51:{'type':r51 ,'left':r49     ,'right':'blank' ,'up':r52     ,'down':'blank' ,'item':'Tesla Coil (Scroll)'  ,'inspect':r51d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r52:{'type':r52 ,'left':r53     ,'right':'blank' ,'up':'blank' ,'down':r51     ,'item':'blank'                ,'inspect':r52d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r52BM},
         r53:{'type':r53 ,'left':'blank' ,'right':r52     ,'up':r54     ,'down':'blank' ,'item':'blank'                ,'inspect':r53d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r54:{'type':r54 ,'left':'blank' ,'right':'blank' ,'up':r76     ,'down':r53     ,'item':'blank'                ,'inspect':r54d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r55:{'type':r55 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r47     ,'item':'Heal Potion (Small)'  ,'inspect':r55d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET ,'size':'large','rest':'n', 'bmap': r55BM},
         r56:{'type':r56 ,'left':r61     ,'right':r46     ,'up':r59     ,'down':r57     ,'item':'blank'                ,'inspect':r56d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r57:{'type':r57 ,'left':'blank' ,'right':'blank' ,'up':r56     ,'down':r58     ,'item':'blank'                ,'inspect':r57d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r57BM},
         r58:{'type':r58 ,'left':'blank' ,'right':'blank' ,'up':r57     ,'down':'blank' ,'item':'Guard Chainmail'      ,'inspect':r58d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r59:{'type':r59 ,'left':r60     ,'right':'blank' ,'up':'blank' ,'down':r56     ,'item':'Acid Bullet (Scroll)' ,'inspect':r59d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r59BM},
         r60:{'type':r60 ,'left':'blank' ,'right':r59     ,'up':r62     ,'down':r61     ,'item':'blank'                ,'inspect':r60d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r60BM},
         r61:{'type':r61 ,'left':'blank' ,'right':r56     ,'up':r60     ,'down':'blank' ,'item':'Web (Scroll)'         ,'inspect':r61d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r62:{'type':r62 ,'left':'blank' ,'right':'blank' ,'up':r63     ,'down':r60     ,'item':'blank'                ,'inspect':r62d ,'map':'f2','minimap':'spiders' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r63:{'type':r63 ,'left':'blank' ,'right':r64     ,'up':'blank' ,'down':r62     ,'item':'blank'                ,'inspect':r63d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r64:{'type':r64 ,'left':r63     ,'right':r65     ,'up':r66     ,'down':'blank' ,'item':'blank'                ,'inspect':r64d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r65:{'type':r65 ,'left':r64     ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Spores (Scroll)'      ,'inspect':r65d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r66:{'type':r66 ,'left':'blank' ,'right':r67     ,'up':r69     ,'down':r64     ,'item':'Food (Large)'         ,'inspect':r66d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r67:{'type':r67 ,'left':r66     ,'right':r68     ,'up':r72     ,'down':'blank' ,'item':'blank'                ,'inspect':r67d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r68:{'type':r68 ,'left':r67     ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Heal Potion (Medium)' ,'inspect':r68d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r69:{'type':r69 ,'left':r71     ,'right':'blank' ,'up':r70     ,'down':r66     ,'item':'blank'                ,'inspect':r69d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r70:{'type':r70 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r69     ,'item':'Shroomal Sythe'       ,'inspect':r70d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r71:{'type':r71 ,'left':'blank' ,'right':r69     ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r71d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r72:{'type':r72 ,'left':'blank' ,'right':r73     ,'up':'blank' ,'down':r67     ,'item':'blank'                ,'inspect':r72d ,'map':'f21','minimap':'shrooms' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r73:{'type':r73 ,'left':r72     ,'right':r74     ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r73d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r74:{'type':r74 ,'left':r73     ,'right':'blank' ,'up':r75     ,'down':'blank' ,'item':'blank'                ,'inspect':r74d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r75:{'type':r75 ,'left':r85     ,'right':r81     ,'up':r88     ,'down':r74     ,'item':'Map (Crossroads)'     ,'inspect':r75d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r76:{'type':r76 ,'left':'blank' ,'right':r78     ,'up':r77     ,'down':r54     ,'item':'blank'                ,'inspect':r76d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r77:{'type':r77 ,'left':'blank' ,'right':r80     ,'up':'blank' ,'down':r76     ,'item':'Food (Medium)'        ,'inspect':r77d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r78:{'type':r78 ,'left':r76     ,'right':r79     ,'up':r80     ,'down':'blank' ,'item':'blank'                ,'inspect':r78d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r79:{'type':r79 ,'left':r78     ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Half Plate'           ,'inspect':r79d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r80:{'type':r80 ,'left':r77     ,'right':'blank' ,'up':r81     ,'down':r78     ,'item':'blank'                ,'inspect':r80d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r81:{'type':r81 ,'left':r75     ,'right':'blank' ,'up':r82     ,'down':r80     ,'item':'blank'                ,'inspect':r81d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r82:{'type':r82 ,'left':'blank' ,'right':r83     ,'up':'blank' ,'down':r81     ,'item':'blank'                ,'inspect':r82d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r83:{'type':r83 ,'left':r82     ,'right':'blank' ,'up':'blank' ,'down':r84     ,'item':'blank'                ,'inspect':r83d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r84:{'type':r84 ,'left':'blank' ,'right':'blank' ,'up':r83     ,'down':'blank' ,'item':'Lightning Dagger'     ,'inspect':r84d ,'map':'f21','minimap':'caves' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r85:{'type':r85 ,'left':'blank' ,'right':r75     ,'up':r86     ,'down':'blank' ,'item':'blank'                ,'inspect':r85d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r86:{'type':r86 ,'left':r90     ,'right':r87     ,'up':r94     ,'down':r85     ,'item':'Heal Potion (Small)'  ,'inspect':r86d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r87:{'type':r87 ,'left':r86     ,'right':r88     ,'up':r89     ,'down':'blank' ,'item':'blank'                ,'inspect':r87d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r88:{'type':r88 ,'left':r87     ,'right':'blank' ,'up':'blank' ,'down':r75     ,'item':'blank'                ,'inspect':r88d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r89:{'type':r89 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r87     ,'item':'Vine Wrap (Scroll)'   ,'inspect':r89d ,'map':'f21','minimap':'mists' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r90:{'type':r90 ,'left':'blank' ,'right':r86     ,'up':'blank' ,'down':r91     ,'item':'Fireball (Scroll)'    ,'inspect':r90d ,'map':'f21','minimap':'parlour' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r91:{'type':r91 ,'left':'blank' ,'right':'blank' ,'up':r90     ,'down':r92     ,'item':'blank'                ,'inspect':r91d ,'map':'f21','minimap':'parlour' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r92:{'type':r92 ,'left':r93     ,'right':'blank' ,'up':r91     ,'down':'blank' ,'item':'blank'                ,'inspect':r92d ,'map':'f21','minimap':'parlour' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r93:{'type':r93 ,'left':'blank' ,'right':r92     ,'up':'blank' ,'down':'blank' ,'item':'Staff of the Magi'    ,'inspect':r93d ,'map':'f21','minimap':'parlour' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r94:{'type':r94 ,'left':'blank' ,'right':r96     ,'up':r95     ,'down':r86     ,'item':'blank'                ,'inspect':r94d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm},
         r95:{'type':r95 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r94     ,'item':'Grand Crown'          ,'inspect':r95d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r96:{'type':r96 ,'left':r94     ,'right':r97     ,'up':'blank' ,'down':'blank' ,'item':'Crown'                ,'inspect':r96d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r97:{'type':r97 ,'left':r96     ,'right':'blank' ,'up':'blank' ,'down':r98     ,'item':'Waterfall (Scroll)'   ,'inspect':r97d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r98:{'type':r98 ,'left':r99     ,'right':'blank' ,'up':r97     ,'down':'blank' ,'item':'blank'                ,'inspect':r98d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r99:{'type':r99 ,'left':'blank' ,'right':r98     ,'up':'blank' ,'down':r100    ,'item':'Food (Medium)'        ,'inspect':r99d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r100:{'type':r100 ,'left':'blank' ,'right':r100tr ,'up':r99    ,'down':'blank' ,'item':'blank'                ,'inspect':r100d ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm},
         r100tr:{'type':r100tr ,'left':r100 ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'blank'             ,'inspect':r100trd ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm}}




items = {'Wood Staff':{'equ':'wea','heal':'n','type':'blunt','pow':10,'def':'n','num':1,'wEquiped':'yes','aEquiped':'no','conditions':'n','weight': 0, 'index': 1, 'sEquiped': 'no', 'aoe': ''},
'Freeze Mist (Scroll)':{'equ':'spe','heal':'n','type':'cold','pow':30,'def':'n','num':1,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'yes', 'aoe': ''},
'Travel Cloak':{'equ':'arm','heal':'n','type':'n','pow':'n','def':10,'num':1,'wEquiped':'no','aEquiped':'yes','conditions':'n','weight': 0, 'index': 2, 'sEquiped': 'no', 'aoe': ''},
'Food (Small)':{'equ':'n','heal':20,'type':'n','pow':'n','def':'n','num':3,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Lantern':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Crown':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Lava Splash (Scroll)':{'equ':'spe','heal':'n','type':'fire','pow':30,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y'},
'Rusty Sword':{'equ':'wea','heal':'n','type':'slash','pow':30,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'index': 3, 'sEquiped': 'no', 'aoe': ''},
'Explosive Charge':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Leather Armour':{'equ':'arm','heal':'n','type':'n','pow':'n','def':20,'num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 0, 'index': 4, 'sEquiped': 'no', 'aoe': ''},
'KEY TO CRIMSON CAVES':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num': 0,'wEquiped':'no','aEquiped':'no','conditions':'y','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Map (Crypts)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Pickaxe':{'equ':'wea','heal':'n','type':'slash','pow':40,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 2, 'index': 5, 'sEquiped': 'no', 'aoe': ''},
'Food (Medium)':{'equ':'n','heal':50,'type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Map (Crimson Caves)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Fire Bolt (Scroll)':{'equ':'spe','heal':'n','type':'fire','pow':60,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Mining Gear':{'equ':'arm','heal':'n','type':'n','pow':'n','def':25,'num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 1, 'index': 6, 'sEquiped': 'no', 'aoe': ''},
'Scorched Chainmail':{'equ':'arm','heal':'n','type':'n','pow':'n','def':35,'num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 3, 'index': 7, 'sEquiped': 'no', 'aoe': ''},
'Steel Sword':{'equ':'wea','heal':'n','type':'slash','pow':50,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 1, 'index': 8, 'sEquiped': 'no', 'aoe': ''},
'Tesla Coil (Scroll)':{'equ':'spe','heal':'n','type':'shock','pow':80,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Heal Potion (Small)':{'equ':'n','heal':40,'type':'n','pow':'n','def':'','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Guard Chainmail':{'equ':'arm','heal':'n','type':'n','pow':'n','def':40,'num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 3, 'index': 9, 'sEquiped': 'no', 'aoe': ''},
'Acid Bullet (Scroll)':{'equ':'spe','heal':'n','type':'acid','pow':70,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Web (Scroll)':{'equ':'spe','heal':'n','type':'acid','pow':10,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y'},
'Spores (Scroll)':{'equ':'spe','heal':'n','type':'acid','pow':45,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y'},
'Shroomal Sythe':{'equ':'wea','heal':'n','type':'acid','pow':45,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'index': 10, 'sEquiped': 'no', 'aoe': ''},
'Food (Large)':{'equ':'n','heal':80,'type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Heal Potion (Medium)':{'equ':'n','heal':60,'type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Map (Crossroads)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Half Plate':{'equ':'arm','heal':'n','type':'n','pow':'n','def':50,'num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 3, 'index': 11, 'sEquiped': 'no', 'aoe': ''},
'Lightning Dagger':{'equ':'wea','heal':'n','type':'shock','pow':55,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': -2, 'index': 12, 'sEquiped': 'no', 'aoe': ''},
'Vine Wrap (Scroll)':{'equ':'spe','heal':'n','type':'nature','pow':55,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Fireball (Scroll)':{'equ':'spe','heal':'n','type':'fire','pow':70,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y'},
'Staff of the Magi':{'equ':'wea','heal':'n','type':'blunt','pow':50,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'index': 13, 'sEquiped': 'no', 'aoe': ''},
'Grand Crown':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''},
'Waterfall (Scroll)':{'equ':'spe','heal':'n','type':'water','pow':80,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': ''}}




def inv(type):
  if items[type]['num'] != 0:
    if items[type]['equ'] == 'wea':
      print( type + '  '+ str(items[type]['num']) + Fore.BLUE +'   pow: ' + str(items[type]['pow']) + '   weight: ' + str(items[type]['weight']))
    elif items[type]['equ'] == 'arm':
      print( type + '  ' +  str(items[type]['num']) + Fore.BLUE +'   def: ' + str(items[type]['def']) + '   weight: ' + str(items[type]['weight']))
    elif items[type]['equ'] == 'spe':
      print( type + '  ' +  str(items[type]['num']) + Fore.BLUE +'   pow: ' + str(items[type]['pow']))
    else:
      print(type + '  ' +  str(items[type]['num']))
    if items[type]['wEquiped'] == 'yes' or items[type]['aEquiped'] == 'yes' or items[type]['sEquiped'] == 'yes':
      print(Fore.RED + '    (equiped)')
    print(Fore.GREEN)


def halt():
  u = input('input any key to continue\n ')


def moveP(dir):
  Player.PreRoom = Player.CRoom
  Player.CRoom = rooms[Player.CRoom][dir]


def runText():
  print(Fore.RED)
  print('\nCurrent Room: ' + rooms[Player.CRoom]['inspect']+'\n')
  if rooms[Player.CRoom]['left'] != 'blank':
    print('left is ' + rooms[Player.CRoom]['left']+'\n')
  if rooms[Player.CRoom]['up'] != 'blank':
    print('up is ' + rooms[Player.CRoom]['up']+'\n')
  if rooms[Player.CRoom]['right'] != 'blank':
    print('right is ' + rooms[Player.CRoom]['right']+'\n')
  if rooms[Player.CRoom]['down'] != 'blank':
    print('down is ' + rooms[Player.CRoom]['down']+'\n')
    
  print(Fore.GREEN)
  print('your current actions are:\ncontrols\nmove (wasd)\ninventory (e)\ninspect (f)\nequip (t)\n')
  
  if rooms[Player.CRoom]['item'] != 'blank':
    print(Fore.RED + 'search (q)' + Fore.GREEN)
    
  if rooms[r4]['item'] == 'blank' and rooms[Player.CRoom]['map'] == 'f1':
    print(Fore.BLUE + 'map (m)')
  elif rooms[r32]['item'] == 'blank' and rooms[Player.CRoom]['map'] == 'f2':
    print(Fore.BLUE + 'map (m)')
  if rooms[Player.CRoom]['rest'] == 'y':
    print(Fore.YELLOW + 'Rest At Safe Room (r),(one time)')
  if rooms[Player.CRoom]['size'] == 'safe':
    print(Fore.YELLOW + 'Heal with items (h)')



def prInv():
  os.system('cls')
  print(Fore.RED)
  print('Health:')
  print(Player.H)
  print(Fore.BLUE+'SP: ')
  print(Player.SP)
  print(Fore.WHITE)
  print('XP: ')
  print(Player.xp)
  print(Fore.GREEN)
   
  inv('Wood Staff')   
  inv('Freeze Mist (Scroll)')
  inv('Travel Cloak')
  inv('Food (Small)')
  inv('Lantern')
  inv('Crown')
  inv('Lava Splash (Scroll)')
  inv('Rusty Sword')
  inv('Explosive Charge')
  inv('Leather Armour')
  inv('KEY TO CRIMSON CAVES')
  inv('Map (Crypts)')
  inv('Pickaxe')
  inv('Food (Medium)')
  inv('Map (Crimson Caves)')
  inv('Fire Bolt (Scroll)')
  inv('Mining Gear')
  inv('Scorched Chainmail')
  inv('Steel Sword')
  inv('Tesla Coil (Scroll)')
  inv('Heal Potion (Small)')
  inv('Guard Chainmail')
  inv('Acid Bullet (Scroll)')
  inv('Web (Scroll)')
  
  
  print(Fore.RESET)


def search():
  if items[rooms[Player.CRoom]['item']]['conditions'] == 'n':
    items[rooms[Player.CRoom]['item']]['num'] = items[rooms[Player.CRoom]['item']]['num'] + 1
    print('\nYou picked up: '+ rooms[Player.CRoom]['item'])
    if Player.CRoom == r13:
      items['Explosive Charge']['num'] = 0
    halt()
    rooms[Player.CRoom]['item'] = 'blank'
  else:
    print('It seems you cant get this item with your current equipment.')
    halt()


def equipable():
  if items['Wood Staff']['num'] != 0:
    print(Fore.GREEN + '                      (1)')
  inv('Wood Staff')
  if items['Travel Cloak']['num'] != 0:
    print(Fore.GREEN + '                      (2)')
  inv('Travel Cloak')
  if items['Rusty Sword']['num'] != 0:
    print(Fore.GREEN + '                      (3)')
  inv('Rusty Sword')
  if items['Leather Armour']['num'] != 0:
    print(Fore.GREEN + '                      (4)')
  inv('Leather Armour')
  if items['Pickaxe']['num'] != 0:
    print(Fore.GREEN + '                      (5)')
  inv('Pickaxe')
  if items['Mining Gear']['num'] != 0:
    print(Fore.GREEN + '                      (6)')
  inv('Mining Gear')
  if items['Scorched Chainmail']['num'] != 0:
    print(Fore.GREEN + '                      (7)')
  inv('Scorched Chainmail')
  if items['Steel Sword']['num'] != 0:
    print(Fore.GREEN + '                      (8)')
  inv('Steel Sword')
  if items['Guard Chainmail']['num'] != 0:
    print(Fore.GREEN + '                      (9)')
  inv('Guard Chainmail')
  if items['Shroomal Sythe']['num'] != 0:
    print(Fore.GREEN + '                      (10)')
  inv('Shroomal Sythe')
  if items['Half Plate']['num'] != 0:
    print(Fore.GREEN + '                      (11)')
  inv('Half Plate')
  if items['Lightning Dagger']['num'] != 0:
    print(Fore.GREEN + '                      (12)')
  inv('Lightning Dagger')
  if items['Staff of the Magi']['num'] != 0:
    print(Fore.GREEN + '                      (13)')
  inv('Staff of the Magi')



def SPequipable():
  if items['Freeze Mist (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (1)')
  inv('Freeze Mist (Scroll)')
  if items['Lava Splash (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (2)')
  inv('Lava Splash (Scroll)')
  if items['Fire Bolt (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (3)')
  inv('Fire Bolt (Scroll)')
  if items['Tesla Coil (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (4)')
  inv('Tesla Coil (Scroll)')
  if items['Acid Bullet (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (5)')
  inv('Acid Bullet (Scroll)')
  if items['Web (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (6)')
  inv('Web (Scroll)')
  if items['Spores (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (7)')
  inv('Spores (Scroll)')
  if items['Vine Wrap (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (8)')
  inv('Vine Wrap (Scroll)')
  if items['Fireball (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (9)')
  inv('Fireball (Scroll)')
  if items['Waterfall (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (10)')
  inv('Waterfall (Scroll)')




def spells():
  if items['Freeze Mist (Scroll)']['num'] == 1 and 'Freeze Mist (Scroll)' in spList:
    print('Freeze Mist (1)')
  if items['Lava Splash (Scroll)']['num'] == 1 and 'Lava Splash (Scroll)' in spList:
    print('Lava Splash (2)')
  if items['Fire Bolt (Scroll)']['num'] == 1 and 'Fire Bolt (Scroll)' in spList:
    print('Fire Bolt (3)')
  if items['Tesla Coil (Scroll)']['num'] == 1 and 'Tesla Coil (Scroll)' in spList:
    print('Tesla Coil (4)')
  if items['Acid Bullet (Scroll)']['num'] == 1 and 'Acid Bullet (Scroll)' in spList:
    print('Acid Bullet (5)')
  if items['Web (Scroll)']['num'] == 1 and 'Web (Scroll)' in spList:
    print('Web (6)')
  if items['Spores (Scroll)']['num'] == 1 and 'Spores (Scroll)' in spList:
    print('Spores (7)')
  if items['Vine Wrap (Scroll)']['num'] == 1 and 'Vine Wrap (Scroll)' in spList:
    print('Vine Wrap (8)')
  if items['Fireball (Scroll)']['num'] == 1 and 'Fireball (Scroll)' in spList:
    print('Fireball (9)')
  if items['Waterfall (Scroll)']['num'] == 1 and 'Waterfall (Scroll)' in spList:
    print('Waterfall (10)')


def heals():
  if items['Food (Small)']['num'] != 0:
    print(Fore.GREEN + str(items['Food (Small)']['num']) +Fore.RESET +'   Food (Small)  (1)')
  if items['Food (Medium)']['num'] != 0:
    print(Fore.GREEN + str(items['Food (Medium)']['num']) +Fore.RESET +'    Food (Medium)  (2)')  
  if items['Food (Large)']['num'] != 0:
    print(Fore.GREEN + str(items['Food (Large)']['num']) +Fore.RESET +'   Food (Large)  (3)')  
  if items['Heal Potion (Small)']['num'] != 0:
    print(Fore.GREEN + str(items['Heal Potion (Small)']['num']) +Fore.RESET +'    Heal Potion (Small)  (4)')
  if items['Heal Potion (Medium)']['num'] != 0:
    print(Fore.GREEN + str(items['Heal Potion (Medium)']['num']) +Fore.RESET +'   Heal Potion (Medium)  (5)')

def playerMove():
  moves = Player.speed - items[Player.weapon]['weight'] - items[Player.armour]['weight']
  while moves != 0:
    com = input('\nDirection (w,a,s,d,wa,wd,sa,sd)\n')
    if com == 'w':
      if Player.CTile - 20 <= 0:
        print('')
      else:
        if screen[Player.CTile - 20]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile -= 20
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap()
    elif com == 's':
      if Player.CTile + 20 > 400:
        print('')
      else:
        if screen[Player.CTile + 20]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile += 20
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap()             
    elif com == 'd':
      if screen[Player.CTile +1]['display'] == '  ':
        if Player.CTile +1 == 21 or Player.CTile +1 == 41 or Player.CTile +1 == 61 or Player.CTile +1 == 81 or Player.CTile +1 == 101 or Player.CTile +1 == 121 or Player.CTile +1 == 141 or Player.CTile +1 == 161 or Player.CTile +1 == 181 or Player.CTile +1 == 201 or Player.CTile +1 == 221 or Player.CTile +1 == 241 or Player.CTile +1 == 261 or Player.CTile +1 == 281 or Player.CTile +1 == 301 or Player.CTile +1 == 321 or Player.CTile +1 == 341 or Player.CTile +1 == 361 or Player.CTile +1 == 381 or Player.CTile +1 == 401: 
          print('')            
        else:
          if screen[Player.CTile +1 ]['display'] == '  ':
            screen[Player.CTile]['display'] = '  '
            Player.CTile += 1
            screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
            os.system('cls')
            print('--Movement Phase--')
            battlemap()            
    elif com == 'a':
      if Player.CTile -1 == 0 or Player.CTile -1 == 20 or Player.CTile -1 == 40 or Player.CTile -1 == 60 or Player.CTile -1 == 80 or Player.CTile -1 == 100 or Player.CTile -1 == 120 or Player.CTile -1 == 140 or Player.CTile -1 == 160 or Player.CTile -1 == 180 or Player.CTile -1 == 200 or Player.CTile -1 == 220 or Player.CTile -1 == 240 or Player.CTile -1 == 260 or Player.CTile -1 == 280 or Player.CTile -1 == 300 or Player.CTile -1 == 320 or Player.CTile -1 == 340 or Player.CTile -1 == 360 or Player.CTile -1 == 380: 
        print('')
      else:
        if screen[Player.CTile - 1]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile -= 1
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap() 
    elif com == 'wa' or com == 'aw':
      if Player.CTile - 20 <= 0 or Player.CTile -1 == 0 or Player.CTile -1 == 20 or Player.CTile -1 == 40 or Player.CTile -1 == 60 or Player.CTile -1 == 80 or Player.CTile -1 == 100 or Player.CTile -1 == 120 or Player.CTile -1 == 140 or Player.CTile -1 == 160 or Player.CTile -1 == 180 or Player.CTile -1 == 200 or Player.CTile -1 == 220 or Player.CTile -1 == 240 or Player.CTile -1 == 260 or Player.CTile -1 == 280 or Player.CTile -1 == 300 or Player.CTile -1 == 320 or Player.CTile -1 == 340 or Player.CTile -1 == 360 or Player.CTile -1 == 380:
        print('')
      else:
        if screen[Player.CTile - 21]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile -= 21
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap()
    elif com == 'wd' or com == 'dw':
      if Player.CTile - 20 <= 0 or Player.CTile +1 == 21 or Player.CTile +1 == 41 or Player.CTile +1 == 61 or Player.CTile +1 == 81 or Player.CTile +1 == 101 or Player.CTile +1 == 121 or Player.CTile +1 == 141 or Player.CTile +1 == 161 or Player.CTile +1 == 181 or Player.CTile +1 == 201 or Player.CTile +1 == 221 or Player.CTile +1 == 241 or Player.CTile +1 == 261 or Player.CTile +1 == 281 or Player.CTile +1 == 301 or Player.CTile +1 == 321 or Player.CTile +1 == 341 or Player.CTile +1 == 361 or Player.CTile +1 == 381 or Player.CTile +1 == 401:
        print('')
      else:
        if screen[Player.CTile - 19]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile -= 19
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap()
    elif com == 'sd' or com == 'ds':
      if Player.CTile + 20 > 400 or Player.CTile -1 == 0 or Player.CTile -1 == 20 or Player.CTile -1 == 40 or Player.CTile -1 == 60 or Player.CTile -1 == 80 or Player.CTile -1 == 100 or Player.CTile -1 == 120 or Player.CTile -1 == 140 or Player.CTile -1 == 160 or Player.CTile -1 == 180 or Player.CTile -1 == 200 or Player.CTile -1 == 220 or Player.CTile -1 == 240 or Player.CTile -1 == 260 or Player.CTile -1 == 280 or Player.CTile -1 == 300 or Player.CTile -1 == 320 or Player.CTile -1 == 340 or Player.CTile -1 == 360 or Player.CTile -1 == 380:
        print('')
      else:
        if screen[Player.CTile + 21]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile += 21
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap()    
    elif com == 'sa' or com == 'as':
      if Player.CTile + 20 > 400 or Player.CTile +1 == 21 or Player.CTile +1 == 41 or Player.CTile +1 == 61 or Player.CTile +1 == 81 or Player.CTile +1 == 101 or Player.CTile +1 == 121 or Player.CTile +1 == 141 or Player.CTile +1 == 161 or Player.CTile +1 == 181 or Player.CTile +1 == 201 or Player.CTile +1 == 221 or Player.CTile +1 == 241 or Player.CTile +1 == 261 or Player.CTile +1 == 281 or Player.CTile +1 == 301 or Player.CTile +1 == 321 or Player.CTile +1 == 341 or Player.CTile +1 == 361 or Player.CTile +1 == 381 or Player.CTile +1 == 401:
        print('')
      else:
        if screen[Player.CTile + 19]['display'] == '  ':
          screen[Player.CTile]['display'] = '  '
          Player.CTile += 19
          screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
          os.system('cls')
          print('--Movement Phase--')
          battlemap()                   
    
    moves -= 1

def spellAttack(enemy):
  if items['Freeze Mist (Scroll)']['num'] == 1 and com == '1' and Player.SP != 0  and 'Freeze Mist (Scroll)' in spList:
    enemy.H -= items['Freeze Mist (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.LIGHTWHITE_EX + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Freeze Mist (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Lava Splash (Scroll)']['num'] == 1 and com == '2'and Player.SP != 0 and 'Lava Splash (Scroll)' in spList:
    enemy.H -= items['Lava Splash (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.LIGHTRED_EX + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Lava Splash (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Fire Bolt (Scroll)']['num'] == 1 and com == '3'and Player.SP != 0 and 'Fire Bolt (Scroll)' in spList:
    enemy.H -= items['Fire Bolt (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.LIGHTRED_EX + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Fire Bolt (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Tesla Coil (Scroll)']['num'] == 1 and com == '4'and Player.SP != 0 and 'Tesla Coil (Scroll)' in spList:
    enemy.H -= items['Tesla Coil (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.BLUE + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Tesla Coil (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Acid Bullet (Scroll)']['num'] == 1 and com == '5'and Player.SP != 0 and 'Acid Bullet (Scroll)' in spList:
    enemy.H -= items['Acid Bullet (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Acid Bullet (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Web (Scroll)']['num'] == 1 and com == '6'and Player.SP != 0 and 'Web (Scroll)' in spList:
    enemy.H -= items['Web (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Web (Scroll)']['pow']) + ' and the enemy has been stuck for 3 turns!')
    WebTimer = 4
    Player.SP -= 1
    halt()
  elif items['Spores (Scroll)']['num'] == 1 and com == '7'and Player.SP != 0 and 'Spores (Scroll)' in spList:
    enemy.H -= items['Spores (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.BLUE + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Spores (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Vine Wrap (Scroll)']['num'] == 1 and com == '8'and Player.SP != 0 and 'Vine Wrap (Scroll)' in spList:
    enemy.H -= items['Vine Wrap (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.LIGHTGREEN_EX + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Vine Wrap (Scroll)']['pow'])+ ' and the enemy has been grappled for 1 turn!')
    WebTimer = 2
    Player.SP -= 1
    halt()
  elif items['Fireball (Scroll)']['num'] == 1 and com == '9'and Player.SP != 0 and 'Fireball (Scroll)' in spList:
    enemy.H -= items['Fireball (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.LIGHTRED_EX + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Fireball (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Waterfall (Scroll)']['num'] == 1 and com == '10'and Player.SP != 0 and 'Waterfall (Scroll)' in spList:
    enemy.H -= items['Waterfall (Scroll)']['pow']
    screen[enemy.ETile]['display'] = Fore.BLUE + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Waterfall (Scroll)']['pow']))
    Player.SP -= 1
    halt()

  else:
    print('Not an option')
    halt()











def fight1(enemy):
  WebTimer = 0
  screen[Player.CTile]['display'] = '  '
  Player.CTile = 250
  for n in screen:
    screen[n]['display'] = '  '
  x = 0
  while x == 0:
    for n in screen:
      if rooms[Player.CRoom]['bmap'][screen[n]['y']][screen[n]['x']] == 1:
        screen[n]['display'] = '##'
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if WebTimer != 0:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
    print('--Movement Phase--')
    battlemap()
    playerMove()
    os.system('cls')
    Player.x = screen[Player.CTile]['x']
    Player.y = screen[Player.CTile]['y']
    enemy.Ex = screen[enemy.ETile]['x']
    enemy.Ey = screen[enemy.ETile]['y']
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if WebTimer != 0:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print(Fore.RED + 'Player Health = ' + str(Player.H) )
    print(Fore.BLUE + 'Player SP = ' + str(Player.SP) + Fore.RESET)
    print(Fore.RED + 'Enemy Health = ' + str(enemy.H))
    print(Fore.RESET + '\n\n\n')
    print('Your turn, options are:\n'+Fore.BLUE+'Flee (f)\nSpell (q)\nItem (e)\nSprint (s)')
    if  Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
      print('Attack (m)')
    com = input()
    if com == 's':
      playerMove()
    elif com == 'm' and Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
      enemy.H -= items[Player.weapon]['pow']



      if items[Player.weapon]['type'] == 'blunt':
        screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'slash':
        screen[enemy.ETile]['display'] = Fore.LIGHTBLUE_EX + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'acid':
        screen[enemy.ETile]['display'] = Fore.GREEN + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'shock':
        screen[enemy.ETile]['display'] = Fore.BLUE + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()


      print('Hits for' + str(items[Player.weapon]['pow']))
      halt()
    elif com == 'f':
      r = random.randint(1,3)
      if r == 3:
        print('Escape Failed!')
        halt()
      else:
        print('Escape Sucessful! Combat ends after Enemy Turn')
        halt()
        Player.CRoom = Player.PreRoom
        x = 1
    elif com == 'q':
      os.system('cls')
      print(Fore.GREEN + 'Your spells are:\n')
      spells()
      com = input('\n\nWhich spell do you cast?')
      spellAttack(enemy)
    elif com == 'e':
      heals()
      com = input()
      if com == '1' and items['Food (Small)']['num'] > 0:
        items['Food (Small)']['num'] -= 1
        Player.H += items['Food (Small)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
          halt()
        else:
          print('Healed ' + str(items['Food (Small)']['heal']))
          halt()
      elif com == '2':
        items['Food (Medium)']['num'] -= 1
        Player.H += items['Food (Medium)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Food (Medium)']['heal']))
        halt()
      elif com == '3':
        items['Food (Large)']['num'] -= 1
        Player.H += items['Food (Large)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Food (Large)']['heal']))
        halt()
      elif com == '4':
        items['Heal Potion (Small)']['num'] -= 1
        Player.H += items['Heal Potion (Small)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Heal Potion (Small)']['heal']))
        halt()
      elif com == '5':
        items['Heal Potion (Medium)']['num'] -= 1
        Player.H += items['Heal Potion (Medium)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Heal Potion (Medium)']['heal']))
        halt()
      else:
        print('not an option')
        halt()
    else:
      print('not an option')
      halt()
    if enemy.H <= 0:
      os.system('cls')
      print('The enemy dies!')
      halt()
      screen[enemy.ETile]['display'] = '  '
      enemy.down = 1
      x = 1
    os.system('cls')
    if enemy.down == 0:
      if WebTimer == 0:
        s = enemy.ESpeed
        while s >= 1:
          if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
            s = 0
          else:
            screen[enemy.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy.ETile]['y'],screen[enemy.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy, 1)
          s -= 1  
        screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'The enemy is stuck!')
        WebTimer -= 1
      print(Fore.RED + '--ENEMY TURN--')
      battlemap()
      if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'The enemy misses!')
        else:
          print(Fore.RED + 'The enemy hits for ' + str(enemy.damage))
          Player.H -= enemy.damage
        print(Fore.RESET)
      halt()
      os.system('cls')
    if Player.H <= 0:
      os.system('cls')
      print('You Died!')
      halt()
      x = 1



















def fight2(enemy,enemy2):
  WebTimer1 = 0
  WebTimer2 = 0
  screen[Player.CTile]['display'] = '  '
  Player.CTile = 250
  for n in screen:
    screen[n]['display'] = '  '
  x = 0
  while x == 0:
    for n in screen:
      if rooms[Player.CRoom]['bmap'][screen[n]['y']][screen[n]['x']] == 1:
        screen[n]['display'] = '##'
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if WebTimer1 != 0:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    if WebTimer2 != 0:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
      screen[enemy2.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
    print('--Movement Phase--')
    battlemap()
    playerMove()
    os.system('cls')
    Player.x = screen[Player.CTile]['x']
    Player.y = screen[Player.CTile]['y']
    enemy.Ex = screen[enemy.ETile]['x']
    enemy.Ey = screen[enemy.ETile]['y']
    enemy2.Ex = screen[enemy2.ETile]['x']
    enemy2.Ey = screen[enemy2.ETile]['y']
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if WebTimer1 != 0:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
    if WebTimer2 != 0:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print(Fore.RED + 'Player Health = ' + str(Player.H) )
    print(Fore.BLUE + 'Player SP = ' + str(Player.SP) + Fore.RESET)
    print(Fore.RED + '\nEnemy 1 Health = ' + str(enemy.H))
    print(Fore.RED + '\nEnemy 2 Health = ' + str(enemy2.H))
    print(Fore.RESET + '\n\n\n')
    print('Your turn, options are:\n'+Fore.BLUE+'Flee (f)\nSpell (q)\nItem (e)\nSprint (s)')
    if  Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
      print('Attack Enemy 1 (m1)')
    if  Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
      print('Attack Enemy 2 (m1)')
    com = input()


    if com == 's':
      playerMove()


    elif com == 'm' or 'm1' and Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
      enemy.H -= items[Player.weapon]['pow']

      if items[Player.weapon]['type'] == 'blunt':
        screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'slash':
        screen[enemy.ETile]['display'] = Fore.LIGHTBLUE_EX + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'acid':
        screen[enemy.ETile]['display'] = Fore.GREEN + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'shock':
        screen[enemy.ETile]['display'] = Fore.BLUE + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()


      print('Hits for' + str(items[Player.weapon]['pow']))
      halt()


    elif com == 'm' or 'm2' and Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
      enemy2.H -= items[Player.weapon]['pow']

      if items[Player.weapon]['type'] == 'blunt':
        screen[enemy2.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'slash':
        screen[enemy2.ETile]['display'] = Fore.LIGHTBLUE_EX + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'acid':
        screen[enemy2.ETile]['display'] = Fore.GREEN + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()
      elif items[Player.weapon]['type'] == 'shock':
        screen[enemy2.ETile]['display'] = Fore.BLUE + '@@' + Fore.RESET
        os.system('cls')
        print(Fore.BLUE + '--Player Turn--')
        battlemap()


      print('Hits for' + str(items[Player.weapon]['pow']))
      halt()

    elif com == 'f':
      r = random.randint(1,3)
      if r == 3:
        print('Escape Failed!')
        halt()
      else:
        print('Escape Sucessful! Combat ends after Enemy Turn')
        halt()
        Player.CRoom = Player.PreRoom
        x = 1


    elif com == 'q':
      os.system('cls')
      print(Fore.GREEN + 'Your spells are:\n')
      spells()
      com = input('\n\nWhich spell do you cast?')
      if enemy.down == 0 and enemy2.down == 0: 
        os.system('cls')
        print('Enemy 1  (1)          Enemy2  (2)')
        com2 = input('Which enemy is the target?')
        if com2 == '1':
          spellAttack(enemy)
        elif com2 == '2':
          spellAttack(enemy2)
        else:
          print('Not an option')
          halt()
      elif enemy.down == 1:
        spellAttack(enemy2)
      else:
        spellAttack(enemy)

 
    elif com == 'e':
      heals()
      com = input()
      if com == '1' and items['Food (Small)']['num'] > 0:
        items['Food (Small)']['num'] -= 1
        Player.H += items['Food (Small)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
          halt()
        else:
          print('Healed ' + str(items['Food (Small)']['heal']))
          halt()
      elif com == '2':
        items['Food (Medium)']['num'] -= 1
        Player.H += items['Food (Medium)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Food (Medium)']['heal']))
        halt()
      elif com == '3':
        items['Food (Large)']['num'] -= 1
        Player.H += items['Food (Large)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Food (Large)']['heal']))
        halt()
      elif com == '4':
        items['Heal Potion (Small)']['num'] -= 1
        Player.H += items['Heal Potion (Small)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Heal Potion (Small)']['heal']))
        halt()
      elif com == '5':
        items['Heal Potion (Medium)']['num'] -= 1
        Player.H += items['Heal Potion (Medium)']['heal']
        if Player.H >= 100:
          Player.H = 100
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Heal Potion (Medium)']['heal']))
        halt()
      else:
        print('not an option')
        halt()
    else:
      print('not an option')
      halt()


    if enemy.H <= 0:
      os.system('cls')
      print('Enemy 1 dies!')
      halt()
      screen[enemy.ETile]['display'] = '  '
      enemy.down = 1

    if enemy2.H <= 0:
      os.system('cls')
      print('Enemy 2 dies!')
      halt()
      screen[enemy2.ETile]['display'] = '  '
      enemy2.down = 1

    if enemy.down == 1 and enemy2.down == 1:
      os.system('cls')
      print('The Enemies are defeated!')
      halt()
      x = 1



    os.system('cls')
    if WebTimer1 == 0:
      s = enemy.ESpeed
      while s >= 1:
        if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
          s = 0
        else:
          screen[enemy.ETile]['display'] = '  '
          astar(rooms[Player.CRoom]['bmap'],(screen[enemy.ETile]['y'],screen[enemy.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy, 2)
        s -= 1  
      screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
      os.system('cls')
    else:
      print(Fore.WHITE + 'Enemy 1 is stuck!')
      WebTimer -= 1

    if WebTimer2 == 0:
      s = enemy2.ESpeed
      while s >= 1:
        if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
          s = 0
        else:
          screen[enemy2.ETile]['display'] = '  '
          astar(rooms[Player.CRoom]['bmap'],(screen[enemy2.ETile]['y'],screen[enemy2.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy2, 2)
        s -= 1  
      screen[enemy2.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
      os.system('cls')
    else:
      print(Fore.WHITE + 'Enemy 2 is stuck!')
      WebTimer2 -= 1



    print(Fore.RED + '--ENEMY TURN--')
    battlemap()
    if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
      hit = random.randint(1,100)
      hit -= items[Player.armour]['def']
      if hit < 1:
        print(Fore.GREEN + 'Enemy 1 misses!')
      else:
        print(Fore.RED + 'Enemy 1 hits for ' + str(enemy.damage))
        Player.H -= enemy.damage
      print(Fore.RESET)

    if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
      hit = random.randint(1,100)
      hit -= items[Player.armour]['def']
      if hit < 1:
        print(Fore.GREEN + 'Enemy 2 misses!')
      else:
        print(Fore.RED + 'Enemy 2 hits for ' + str(enemy2.damage))
        Player.H -= enemy2.damage
      print(Fore.RESET)
      
    halt()
    os.system('cls')
    if Player.H <= 0:
      os.system('cls')
      print('You Died!')
      halt()
      x = 1






def resetcolours():
  rooms[r0]['mmc'] = Fore.RESET
  rooms[r1]['mmc'] = Fore.RESET
  rooms[r2]['mmc'] = Fore.RESET
  rooms[r3]['mmc'] = Fore.RESET
  rooms[r4]['mmc'] = Fore.RESET
  rooms[r5]['mmc'] = Fore.RESET
  rooms[r6]['mmc'] = Fore.RESET
  rooms[r7]['mmc'] = Fore.RESET
  rooms[r8]['mmc'] = Fore.YELLOW
  rooms[r9]['mmc'] = Fore.RESET
  rooms[r10]['mmc'] = Fore.RESET
  rooms[r11]['mmc'] = Fore.RESET
  rooms[r12]['mmc'] = Fore.RESET
  rooms[r13]['mmc'] = Fore.RESET
  rooms[r14]['mmc'] = Fore.RESET
  rooms[r15]['mmc'] = Fore.RESET
  rooms[r16]['mmc'] = Fore.RESET
  rooms[r17]['mmc'] = Fore.RESET
  rooms[r18]['mmc'] = Fore.RESET
  rooms[r19]['mmc'] = Fore.RESET
  rooms[r20]['mmc'] = Fore.RESET
  rooms[r21]['mmc'] = Fore.RESET
  rooms[r22]['mmc'] = Fore.RESET
  rooms[r23]['mmc'] = Fore.RESET
  rooms[r24]['mmc'] = Fore.RESET
  rooms[r25]['mmc'] = Fore.RESET
  rooms[r26]['mmc'] = Fore.RESET
  rooms[r27]['mmc'] = Fore.RESET
  rooms[r28]['mmc'] = Fore.RESET
  rooms[r29]['mmc'] = Fore.RESET
  rooms[r30]['mmc'] = Fore.RESET
  rooms[r31]['mmc'] = Fore.RESET
  rooms[r32]['mmc'] = Fore.YELLOW
  rooms[r33]['mmc'] = Fore.RESET
  rooms[r34]['mmc'] = Fore.RESET
  rooms[r35]['mmc'] = Fore.RESET
  rooms[r36]['mmc'] = Fore.RESET
  rooms[r37]['mmc'] = Fore.RESET
  rooms[r38]['mmc'] = Fore.RESET
  rooms[r39]['mmc'] = Fore.RESET
  rooms[r40]['mmc'] = Fore.RESET
  rooms[r41]['mmc'] = Fore.RESET
  rooms[r42]['mmc'] = Fore.RESET
  rooms[r43]['mmc'] = Fore.RESET
  rooms[r44]['mmc'] = Fore.RESET
  rooms[r45]['mmc'] = Fore.YELLOW
  rooms[r46]['mmc'] = Fore.RESET
  rooms[r47]['mmc'] = Fore.RESET
  rooms[r48]['mmc'] = Fore.RESET
  rooms[r49]['mmc'] = Fore.RESET
  rooms[r50]['mmc'] = Fore.RESET
  rooms[r51]['mmc'] = Fore.RESET
  rooms[r52]['mmc'] = Fore.RESET
  rooms[r53]['mmc'] = Fore.YELLOW
  rooms[r54]['mmc'] = Fore.RESET
  rooms[r55]['mmc'] = Fore.RESET
  rooms[r56]['mmc'] = Fore.RESET
  rooms[r57]['mmc'] = Fore.RESET
  rooms[r58]['mmc'] = Fore.RESET
  rooms[r59]['mmc'] = Fore.RESET
  rooms[r60]['mmc'] = Fore.RESET
  rooms[r61]['mmc'] = Fore.RESET
  rooms[r62]['mmc'] = Fore.YELLOW
  rooms[r63]['mmc'] = Fore.RESET
  rooms[r64]['mmc'] = Fore.RESET
  rooms[r65]['mmc'] = Fore.RESET
  rooms[r66]['mmc'] = Fore.RESET
  rooms[r67]['mmc'] = Fore.RESET
  rooms[r68]['mmc'] = Fore.RESET
  rooms[r69]['mmc'] = Fore.RESET
  rooms[r70]['mmc'] = Fore.RESET
  rooms[r71]['mmc'] = Fore.RESET
  rooms[r72]['mmc'] = Fore.RESET
  rooms[r73]['mmc'] = Fore.RESET
  rooms[r74]['mmc'] = Fore.RESET
  rooms[r75]['mmc'] = Fore.RESET
  rooms[r76]['mmc'] = Fore.RESET
  rooms[r77]['mmc'] = Fore.RESET
  rooms[r78]['mmc'] = Fore.RESET
  rooms[r79]['mmc'] = Fore.RESET
  rooms[r80]['mmc'] = Fore.RESET
  rooms[r81]['mmc'] = Fore.RESET
  rooms[r82]['mmc'] = Fore.RESET
  rooms[r83]['mmc'] = Fore.RESET
  rooms[r84]['mmc'] = Fore.RESET
  rooms[r85]['mmc'] = Fore.RESET
  rooms[r86]['mmc'] = Fore.RESET
  rooms[r87]['mmc'] = Fore.RESET
  rooms[r88]['mmc'] = Fore.RESET
  rooms[r89]['mmc'] = Fore.RESET
  rooms[r90]['mmc'] = Fore.RESET
  rooms[r91]['mmc'] = Fore.RESET
  rooms[r92]['mmc'] = Fore.RESET
  rooms[r93]['mmc'] = Fore.RESET
  rooms[r94]['mmc'] = Fore.RESET
  rooms[r95]['mmc'] = Fore.RESET
  rooms[r96]['mmc'] = Fore.RESET
  rooms[r97]['mmc'] = Fore.RESET
  rooms[r98]['mmc'] = Fore.RESET
  rooms[r99]['mmc'] = Fore.RESET
  rooms[r100]['mmc'] = Fore.RESET
  rooms[r100tr]['mmc'] = Fore.RESET
  

def enc1(enemy):
  print('You encountered '+Fore.RED + enemy.name)
  x = 0
  while x == 0:
    com = input('What action:'+Fore.BLUE+' \nRun (r)\n'+Fore.RED+'Fight  (f)'+Fore.RESET+'\n\n')

    if com == 'Run' or com == 'r':
      r = random.randint(1,6)
      if r != 6:
        Player.CRoom = Player.PreRoom
        print('Ran successfuly')
        halt()
        x = 1
      else:
        print('Failed, combat is engaged')
        halt()
        os.system('cls')
        fight1(enemy)
        x = 1
    elif com == 'Fight' or com == 'f':
      os.system('cls')
      fight1(enemy)
      x = 1
    else:
     print('not an option')
     os.system('cls')
 
def enc2(enemy,enemy2):
  print('You encountered '+Fore.RED + enemy.name + ' and ' + enemy2.name)
  x = 0
  while x == 0:
    com = input('What action:'+Fore.BLUE+' \nRun (r)\n'+Fore.RED+'Fight  (f)'+Fore.RESET+'\n\n')

    if com == 'Run' or com == 'r':
      r = random.randint(1,6)
      if r != 6:
        Player.CRoom = Player.PreRoom
        print('Ran successfuly')
        halt()
        x = 1
      else:
        print('Failed, combat is engaged')
        halt()
        os.system('cls')
        fight2(enemy, enemy2)
        x = 1
    elif com == 'Fight' or com == 'f':
      os.system('cls')
      fight2(enemy, enemy2)
      x = 1
    else:
     print('not an option')
     os.system('cls')






spList = ['Freeze Mist (Scroll)']
class P:
  def __init__(self,CRoom,H,weapon,armour,PreRoom,CTile,SP,x,y,speed,xp,level,maxH,spellSL,spellList):
    self.CRoom = CRoom
    self.H = H
    self.weapon = weapon
    self.armour = armour
    self.PreRoom = PreRoom
    self.CTile = CTile
    self.SP = SP
    self.x = x
    self.y = y
    self.speed = speed
    self.xp = xp
    self.level = level
    self.maxH = maxH
    self.spellSL =spellSL
    self.spellList = spellList
Player = P(r0,100,'Wood Staff','Travel Cloak',r0,250,3,1,1,3,0,1,100,3,spList)
print(Fore.BLUE)
print('Welcome to the game,   controls are:\n w a s d   for movement,\ne   for inventory,\nq   for search,\nf   for inspect,\nm   for map (if you have one in the area)\nt    for equip (then the index number)    ')
print('\nIf you forget any controls, you can also spell out the action you want to take')
halt()
print(Fore.RESET)
os.system('cls')

y=0
while y == 0:
  if Player.H <= 0:
    break
  resetcolours()
  rooms[Player.CRoom]['mmc'] = Fore.GREEN
  if Enemy0A.down == 0:
    rooms[Enemy0A.ERoom]['mmc'] = Fore.RED
  if Enemy1.down == 0:
    rooms[Enemy1.ERoom]['mmc'] = Fore.RED
  if Enemy2.down == 0:
    rooms[Enemy2.ERoom]['mmc'] = Fore.RED
  if Enemy3.down == 0:
    rooms[Enemy3.ERoom]['mmc'] = Fore.RED
  if Enemy4.down == 0:
    rooms[Enemy4.ERoom]['mmc'] = Fore.RED
  if Enemy5.down == 0:
    rooms[Enemy5.ERoom]['mmc'] = Fore.RED
  if Enemy6.down == 0:
    rooms[Enemy6.ERoom]['mmc'] = Fore.RED
  if Enemy7.down == 0:
    rooms[Enemy7.ERoom]['mmc'] = Fore.RED
  if Enemy8.down == 0:
    rooms[Enemy8.ERoom]['mmc'] = Fore.RED
  if Sen1.down == 0:
    rooms[Sen1.ERoom]['mmc'] = Fore.RED
  if Sen2.down == 0:
    rooms[Sen2.ERoom]['mmc'] = Fore.RED
  
  if rooms[Player.CRoom]['minimap'] == 'ice':
    ice_caves()
  elif rooms[Player.CRoom]['minimap'] == 'crypt':
    crypts()
  elif rooms[Player.CRoom]['minimap'] == 'wastes':
    wastes()
  elif rooms[Player.CRoom]['minimap'] == 'deltas':
    deltas()
  elif rooms[Player.CRoom]['minimap'] == 'lockhouse':
    lockhouse()
  elif rooms[Player.CRoom]['minimap'] == 'spiders':
    spiders()
  elif rooms[Player.CRoom]['minimap'] == 'shrooms':
    shrooms()
  elif rooms[Player.CRoom]['minimap'] == 'caves':
    caves()
  elif rooms[Player.CRoom]['minimap'] == 'mists':
    mists()
  elif rooms[Player.CRoom]['minimap'] == 'parlour':
    parlour()
  elif rooms[Player.CRoom]['minimap'] == 'river':
    river()
  runText()
  
  
  x=0
  while x==0:
    
    com = input(Fore.BLUE + "-< Input >- \n\n")

    
    if com == 'up' and rooms[Player.CRoom]['up'] != 'blank'  or com == 'w' and rooms[Player.CRoom]['up'] != 'blank':
      moveP('up')
      x = 1
    elif com == 'down' and rooms[Player.CRoom]['down'] != 'blank' or com == 's' and rooms[Player.CRoom]['down'] != 'blank':
      moveP('down')
      x = 1
    elif com == 'left' and rooms[Player.CRoom]['left'] != 'blank' or com == 'a' and rooms[Player.CRoom]['left'] != 'blank' :
      moveP('left')
      x = 1
    elif com == 'right' and rooms[Player.CRoom]['right'] != 'blank' or com == 'd' and rooms[Player.CRoom]['right'] != 'blank':
      moveP('right')
      x = 1



    
    elif com == 'inventory' or com == 'e':
      prInv()
      halt()
      x = 1


    
    elif com == 'search' and rooms[Player.CRoom]['item'] != 'blank' or com == 'q' and rooms[Player.CRoom]['item'] != 'blank':
      search()
      x = 1


    elif com == 'inspect' or com == 'f':
      os.system('cls')
      print(rooms[Player.CRoom]['inspect'])
      halt()
      x = 1


    
    elif com == 'map' or com == 'm':
      os.system('cls')
      if rooms[r4]['item'] == 'blank' and rooms[Player.CRoom]['map'] == 'f1':
        bigmapOne()
        halt()
        x = 1
      elif rooms[r32]['item'] == 'blank' and rooms[Player.CRoom]['map'] == 'f2':
        bigmapTwoOne()
        halt()
        x = 1
    

    elif com == 'equip' or com ==  't':
      print(Fore.GREEN)
      os.system('cls')
      com = input('What category?\n\nWeapons + Armours   (1)\n\nSpells   (2)   ')
      if com == '1':
        os.system('cls')
        equipable()
        com2 = input('What item would you like to equip?    ')
        if com2 == '1':
          com2 = 'Wood Staff'
        if com2 == '2':
          com2 = 'Travel Cloak'
        if com2 == '3':
          com2 = 'Rusty Sword'
        if com2 == '4':
          com2 = 'Leather Armour'
        if com2 == '5':
          com2 = 'Pickaxe'
        if com2 == '6':
          com2 = 'Mining Gear'
        if com2 == '7':
          com2 = 'Scorched Chainmail'
        if com2 == '8':
          com2 = 'Steel Sword'
        if com2 == '9':
          com2 = 'Guard Chainmail'
        if com2 == '10':
          com2 = 'Shroomal Sythe'
        if com2 == '11':
          com2 = 'Half Plate'
        if com2 == '12':
          com2 = 'Lightning Dagger'
        if com2 == '13':
          com2 = 'Staff of the Magi'

        if com2 in items:
          if items[com2]['num'] != 0:
            if items[com2]['equ'] == 'wea':
              items[Player.weapon]['wEquiped'] = 'no'
              items[com2]['wEquiped'] = 'yes'
              Player.weapon = com2
              print('Equiped '+com2)
              halt()
              x = 1
            if items[com2]['equ'] == 'arm':
              items[Player.armour]['aEquiped'] = 'no'
              items[com2]['aEquiped'] = 'yes'
              Player.armour = com2
              print('Equiped '+com2)
              halt()
              x = 1
          else:
            print('not an option')
            halt()
            x = 1
        else:
          print('not an option')
          halt()
          x = 1
      elif com == '2':
        os.system('cls')
        SPequipable()
        com2 = input('What item would you like to equip?    ')
        if com2 == '1':
          com2 = 'Freeze Mist (Scroll)'
        if com2 == '2':
          com2 = 'Lava Splash (Scroll)'
        if com2 == '3':
          com2 = 'Fire Bolt (Scroll)'
        if com2 == '4':
          com2 = 'Tesla Coil (Scroll)'
        if com2 == '5':
          com2 = 'Acid Bullet (Scroll)'
        if com2 == '6':
          com2 = 'Web (Scroll)'
        if com2 == '7':
          com2 = 'Spores (Scroll)'
        if com2 == '8':
          com2 = 'Vine Wrap (Scroll)'
        if com2 == '9':
          com2 = 'Fireball (Scroll)'
        if com2 == '10':
          com2 = 'Waterfall (Scroll)'
        if com2 in items:
          if items[com2]['num'] != 0:
            if len(spList) < Player.spellSL:
              if com2 in spList:
                print('Already equiped')
                halt()
                x = 1
              else:
                items[com2]['sEquiped'] = 'yes'
                spList.append(com2)
                print('Equiped '+com2)
                halt()
                x = 1
            else:
              print(spList)
              if len(spList) == 1:
                print('   (1)')
              if len(spList) == 2:
                print('   (1)                       (2)')
              if len(spList) == 3:
                print('   (1)                       (2)                       (3)')
              if len(spList) == 4:
                print('   (1)                       (2)                       (3)                       (4)')

              com3 = input('\nSpell list full, which item do you want to remove?   ')
              if com3 == '1':
                com3 = spList[0]
              elif com3 == '2' and len(spList) <= 2:
                com3 = spList[1]
              elif com3 == '3' and len(spList) <= 3:
                com3 = spList[2]
              elif com3 == '4' and len(spList) <= 4:
                com3 = spList[3]

              if com3 in spList:
                spList.remove(com3)
                items[com3]['sEquiped'] = 'no'
                if com2 in spList:
                  print('Already equiped')
                  halt()
                  x = 1
                else:
                  items[com2]['sEquiped'] = 'yes'
                  spList.append(com2)
                  print('Equiped '+com2)
                  halt()
                  x = 1
              else:
                print('not an option')
                halt()
                x = 1
          else:
            print('not an option')  
            halt()
            x = 1
        else:
          print('not an option')  
          halt()
          x = 1

    elif com == 'r' and rooms[Player.CRoom]['rest'] == 'y':
      rooms[Player.CRoom]['rest'] = 'n'
      print('Health and SP restored')
      Player.SP = Player.spellSL
      Player.H = Player.maxH
      halt()
      x = 1
    elif com == 'h' and rooms[Player.CRoom]['size'] == 'safe':
      heals()
      com = input()
      if com == '1' and items['Food (Small)']['num'] > 0:
        items['Food (Small)']['num'] -= 1
        Player.H += items['Food (Small)']['heal']
        if Player.H >= Player.maxH:
          Player.H = Player.maxH
          print(Fore.GREEN + 'Healed to full!')
          halt()
        else:
          print('Healed ' + str(items['Food (Small)']['heal']))
          halt()
      elif com == '2':
        items['Food (Medium)']['num'] -= 1
        Player.H += items['Food (Medium)']['heal']
        if Player.H >= Player.maxH:
          Player.H = Player.maxH
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Food (Medium)']['heal']))
        halt()
      elif com == '3':
        items['Food (Large)']['num'] -= 1
        Player.H += items['Food (Large)']['heal']
        if Player.H >= Player.maxH:
          Player.H = Player.maxH
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Food (Large)']['heal']))
        halt()
      elif com == '4':
        items['Heal Potion (Small)']['num'] -= 1
        Player.H += items['Heal Potion (Small)']['heal']
        if Player.H >= Player.maxH:
          Player.H = Player.maxH
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Heal Potion (Small)']['heal']))
        halt()
      elif com == '5':
        items['Heal Potion (Medium)']['num'] -= 1
        Player.H += items['Heal Potion (Medium)']['heal']
        if Player.H >= Player.maxH:
          Player.H = Player.maxH
          print(Fore.GREEN + 'Healed to full!')
        else:
          print('Healed ' + str(items['Heal Potion (Medium)']['heal']))
        halt()
      else:
        print('not an option')
        halt()
      x = 1


    elif com == 'controls':
      print('controls are:\n w a s d   for movement,\ne   for inventory,\nq   for search,\nf   for inspect,\nm   for map (if you have one in the area)\nt    for equip (then the name of the item, which is case sensitive)    ')


    else:
      print("not an option\n")
      halt()
      x = 1
 
  print(Fore.RESET)
  os.system('cls')



 
  if Player.CRoom == Enemy0A.ERoom and Enemy0A.down == 0 and Enemy0B.down == 0:
    enc2(Enemy0A,Enemy0B)
    Player.xp  += Enemy0A.XP
    os.system('cls')
    print('Gained ' + str(Enemy0A.XP) + 'XP points!')
  if Player.CRoom == Enemy1.ERoom and Enemy1.down == 0:
    enc1(Enemy1)  
    Player.xp  += Enemy1.XP
    os.system('cls')
    print('Gained ' + str(Enemy1.XP) + 'XP points!')
  if Player.CRoom == Enemy2.ERoom and Enemy2.down == 0:
    enc1(Enemy2)  
    Player.xp  += Enemy2.XP
    os.system('cls')
    print('Gained ' + str(Enemy2.XP) + 'XP points!')
  if Player.CRoom == Enemy3.ERoom and Enemy3.down == 0:
    enc1(Enemy3)  
    Player.xp  += Enemy3.XP
    os.system('cls')
    print('Gained ' + str(Enemy3.XP) + 'XP points!')
  if Player.CRoom == Enemy4.ERoom and Enemy4.down == 0:
    enc1(Enemy4)  
    Player.xp  += Enemy4.XP
    os.system('cls')
    print('Gained ' + str(Enemy4.XP) + 'XP points!')
  if Player.CRoom == Enemy5.ERoom and Enemy5.down == 0:
    enc1(Enemy5)  
    Player.xp  += Enemy5.XP
    os.system('cls')
    print('Gained ' + str(Enemy5.XP) + 'XP points!')
  if Player.CRoom == Enemy6.ERoom and Enemy6.down == 0:
    enc1(Enemy6)  
    Player.xp  += Enemy6.XP
    os.system('cls')
    print('Gained ' + str(Enemy6.XP) + 'XP points!')
  if Player.CRoom == Enemy7.ERoom and Enemy7.down == 0:
    enc1(Enemy7)  
    Player.xp  += Enemy7.XP
    os.system('cls')
    print('Gained ' + str(Enemy7.XP) + 'XP points!')
  if Player.CRoom == Enemy8.ERoom and Enemy8.down == 0:
    enc1(Enemy8)  
    Player.xp  += Enemy8.XP
    os.system('cls')
    print('Gained ' + str(Enemy8.XP) + 'XP points!')
  if Player.CRoom == Sen1.ERoom and Sen1.down == 0:
    enc1(Sen1) 
    Player.xp  += Sen1.XP
    os.system('cls')
    print('Gained ' + str(Sen1.XP) + 'XP points!')
  if Player.CRoom == Sen2.ERoom and Sen2.down == 0:
    enc1(Sen2) 
    Player.xp  += Sen2.XP
    os.system('cls')
    print('Gained ' + str(Sen2.XP) + 'XP points!')







  if Player.xp >= 40 and Player.level < 2:
    print('You leveled up to LVL 2!\nHP increases by 20')
    Player.level = 2
    Player.maxH += 20
    Player.H += 20
  if Player.xp >= 130 and Player.level < 3:
    print('You leveled up to LVL 3!\nHP increases by 20   and   Gain 1 Max SP')
    Player.level = 3
    Player.maxH += 20
    Player.H += 20
    Player.spellSL += 1
    Player.SP += 1    
  if Player.xp >= 300 and Player.level < 4:
    print('You leveled up to LVL 4!\nHP increases by 20')
    Player.level = 4
    Player.maxH += 20
    Player.H += 20
  if Player.xp >= 400 and Player.level < 5:
    print('You leveled up to LVL 5!\nHP increases by 20   and   Gain 1 Base Speed')
    Player.level = 5
    Player.maxH += 20
    Player.H += 20
    Player.speed += 1








  if items['Lantern']['num'] == 1 and items['Explosive Charge']['num'] == 1:
    items['KEY TO CRIMSON CAVES']['conditions'] = 'n'
  if r25KeyText == 'y':  
    if Player.CRoom == r25:
      if items['KEY TO CRIMSON CAVES']['conditions'] == 'n':
        print('You take the key, and put it in the slot in the door. It glows with green light which flows through the   markings in the door. It rumbles open, revealing a passageway to the CRIMSON MINES, the next stop on your journey down the dungeon. As you walk through, it closes behind you, with a similar keyhole on this side, though you know that you need to press onwards for now.')
        halt()
        os.system('cls')
        r25KeyText = 'n'
        rooms[r25]['right'] = r26
      else:
        print(Fore.RED + 'A key is needed for this path\n')
        print(Fore.RESET)


