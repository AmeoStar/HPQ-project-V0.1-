from colorama import Fore
import os
import random     
from colored import fg




r25KeyText = 'y'


r0 = 'a small cave with a large, ornate doorway'
r1 = 'a tall cave with icicles hanging in the celing'
r2 = 'a cave split in two by a ravine'
r3 = 'a dark passage leading to a small hollow'
r4 = 'a built up stone structure with a treasure chest'
r5 = 'a huge cave with ice-covered trees and a half frozen river'
r6 = 'a thin hallway with water covering the centre '
r7 = 'a hostile room with large icicles on the floor and celing'
r8 = 'a small nook'
r9 = 'a medium sized cave, with a pond in the centre'
r10 = 'a large hallway cave, with a split path through'
r11 = 'an old garrison, with a few non-rusted weapons on a rack'
r12 = 'a huge cave, with a large depth charge mining setup'
r13 = 'a small cave with an ancient looking key frozen behind ice.'
r14 = 'a smaller hollow, with a stone door to the crypts'
r15 = 'a large war room, with a round table at its centre.'
r16 = 'a large, central area that serves as an entrance to the crypts'
r17 = 'a huge room, with two staircases either side leading to a second floor.'
r18 = 'an old forge, with 3 large containers of lava'
r19 = 'a smaller connecting room, with a gap that shows a long room with pillars'
r20 = 'a room hidden by a painting'
r21 = 'a winding, connecting passage with various different murals on the walls'
r22 = 'a side room, with equipment and more murals inside'
r23 = 'a small connecting room'
r24 = 'a huge hallway, lined with pillars with an impressive statue of a king'
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
r67 = 'a stone house ruin with campfire smoke rising from within'
r68 = 'a storage area for the encampment'
r69 = 'a shroom-filled passageway'
r70 = 'a small hut built into one of the mushrooms'
r71 = 'a large house, resembeling a blue pumpkin'
r72 = 'a built up room with a portcullis smashed out of its hinges.'
r73 = 'a misty passageway'
r74 = 'a small, cold cave with heavy smoke covering the floor'
r75 = 'an enourmous cave, with a huge stone bridge crossing the expanse'
r76 = 'a densely packed caveway full of winding passages'
r77 = 'a dark set of passages, with water on the floor'
r78 = 'a spiked room full of spindly rocks'
r79 = 'a small hideaway with a cloth draping door'
r80 = 'a long pasageway with walls covered in glowing green gems'
r81 = 'a forked cave, with three total routes'
r82 = 'an entranceway to a chrome building'
r83 = 'a densely packed experiment space, containing various vials'
r84 = 'a room with cords hanging down, conecting to large iron automatons'
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
r101 = 'a damp, flooded cave'
r102 = 'a connecting cove'
r103 = 'the ruins of a small dock'
r104 = 'a ruined cargo hold'
r105 = 'a "special items" holding area'
r106 = 'a large dock cave'
r107 = 'a boathouse'
r108 = 'a large open cavern filled with water'
r109 = 'a shallow lagoon cave'
r110 = 'an enourmous lake with an old galley boat'
r111 = 'a small raft with rigging to the bottom deck'
r112 = 'the gun deck of the ship'
r113 = 'a storage hold'
r114 = 'the captains cabin'
r115 = 'the main deck of the ship'
r116 = 'the crows nest'
r117 = 'the back deck'
r118 = 'a small side bay'
r119 = 'a spiky bay'
r120 = 'a rocky connecting path'
r121 = 'a weapons staging cannonhold'
r122 = 'a small stone building'
r123 = 'a cave full of shipwrecks'
r124 = 'a small passageway'
r125 = 'a little wooden hut'
r126 = 'an eerie open cave'
r127 = '-TO THE BLACK MINES- a mineshaft with a winch lift'
r128 = '-TO THE UPPER LAKES- a mineshaft with a winch lift'
r129 = 'a dark, foggy opening'
r130 = 'a long cave with wooden struts holding it up'
r131 = 'a collapsed mineshaft'
r132 = 'an open connecting cave'
r133 = 'a small crack in the mine wall'
r134 = 'a lakeside cave'
r135 = 'an entrance patio to a wooden building'
r136 = 'the entrance hall for the house'
r137 = 'a creaking hallway with a suits of armour standing'
r138 = 'a balcony looking out to the lake'
r139 = 'an entertainment room with faded furnishings'
r140 = 'a hidden passageway'
r141 = 'a secret meeting room'
r142 = 'a long wooden hallway lined with paintings'
r143 = 'a fancy bedroom'
r144 = 'a large set of gates made of black iron'
r145 = '145'
r146 = '146'
r147 = '147'
r148 = '148'
r149 = '149'
r150 = '150'
r151 = '151'
r152 = '152'
r153 = '153'
r154 = '154'
r155 = '155'
r156 = '156'
r157 = '157'
r158 = '158'
r159 = '159'
r160 = '160'
r161 = '161'
r162 = '162'
r163 = '163'
r164 = '164'
r165 = '165'
r166 = '166'
r167 = '167'
r168 = '168'





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
r63d = 'The floor is surprisingly springy, and the blue, unnatural glow illuminates the cave in haunting light. The tree-like mushrooms claw at all surfaces, grasping them with their tendrils. A musky smell permeates the air.'
r64d = 'As you look at the stream before you, you notice its liquid runs thicker than usual, and effervescent blue colour and thick. Smaller mushrooms cover the floor and walls like moss.'
r65d = 'A strange stone encampment surrounds you, tiny and claustrophobic, with little mushroom caps covering the walls and putting a fine green powder in the air. It doesnt feel like a good idea to stay for long.'
r66d = 'The forest around you is made up completely of giant mushroom caps, their glow lights up the large cavern. Dark blue vines hang from the mushroom caps, making it hard to see through the dense mass.'
r67d = 'The house has only one wall standing; the one at the far end which borders a smaller cave. The others lie on the floor in ruins, though some wooden poles and cloth have been put up in their place. There is evidence of several feverent repair jobs done to the site.'
r68d = 'It feels like a safe, the small cave provides a lot of protection from the accumulating damages of the main building. It is the most unorganised place you have ever seen, the volume of noise present is quite impressive.'
r69d = 'Glow from the forest puts the corridor in a haunting light. Darkness envelops it at the far end.'
r70d = 'It is hard to notice the little hollow, to call it a living space for anything more than a fox is a stretch. A collection of items, both mundane and interesting, cover its little floor.'
r71d = 'The interior of the house is quite nice for the area its in, carved wooden furniture and bookshelves full of scrolls and tomes fill the walls. A cast iron pot sits in the corner.'
r72d = 'This looks like it used to be a heavily fortified point long in the past, but now it lies derilect. A resounding stone doorway now cracked with moss, though the damage to its top where the iron portcullis was blown away doesnt look to be the work of time.'
r73d = 'The passageway floor is a lined cobble road, destroyed in some spots but mostly walkable. The thick fog billowing from the other chamber makes vision limited.'
r74d = 'Smoke billows around your boots, blowing as a foul stench from the further passageways. A damp chill wafts through the air, the barren dark lit meagerly by your lantern.'
r75d = 'The grand scale of the cavern reaches so high up, the ice starts to creep back in further towards the top, and you can see connecting passageways from different parts of the first layer you descendef from. You are about halfway down the cave, it descends to a dark, glimmering abyss, haunting lights flickering over grimy blackstone passageways. You dread to imagine what lies down there. On this section, the large crossroads bridge connects to four total areas on each side of the cavern. The death like fog is billowing up from below.'
r76d = 'At several points while exploring the area, you find yourself lost and looped back upon yourself. The layout resembles mole holes in a way, vaguely cylinder shaped and looping back, connecting to each other.'
r77d = 'The water comes up to your knees at its deepest. Its an opressive atmosphere, sounds from other dark passages too high up for you to reach sending chills down your spine.'
r78d = 'The rocks stick out from different angles in the walls. Some pillar like structures stretch like needles from the floor and celing. Despite the hostile feel, it is nice and open, compared to the other winding tubes.'
r79d = 'You recognise the room as another cartographers hollow, as expected a map of the caves is inside. It looks like it was left very recently, only a day or so ago. You must be following quite close behind whoever has been making these maps.'
r80d = 'On either side of the corridor are pits that fall down to a further section you assume is in the floors below. A similar maze of crystals like the ones here give a glow in the darkness. Small slits line the far walls, this must have been a defensable location in the past. They lie empty now.'
r81d = 'A thick mist billows from the large chamber, which disperses into strange iron vents on the eastern wall.'
r82d = 'The door is built into the stone, and is still functioning. It looks to be made of a mix of marble and silvery metals.'
r83d = 'You are careful when walking around as to not knock any of the vials over. Some expensive looking cogwork and steam pumps whir the intricate systems around the lab in motion; it is self sustaining. Glowing white lanterns line the celing, and are made of pure white crystal.'
r84d = 'The main testing area, several parts of automatons lie all around. You can only imagine what kind of person would set such a place up down in these dangerous depths.'
r85d = 'The fog here is different from that of earlier in the caves, it holds a sticky, hot air that makes your clothes stick uncomfortably to your skin. The roadways here lead into an area of dense greenery that spills into this chamber.'
r86d = 'A murky, warm green water swirls around your ankles. The cave towers up and up, with vines as thick as a person hanging heavy on the stone celing. It feels like a sauna, the steam circulating around the chamber, foliage stopping it from escaping into the other routes.'
r87d = 'While not as thick, dense dark green moss covers the cave like fur, warm swamp water swirling around your feet.'
r88d = 'There is receeding greenery in this section, mist blowing in from the southern cavern. Muddy water is containded in a pool funneled to the western chamber'
r89d = 'It looks like it hasnt been looked at in a while, the swamp vegetation has destroyed most of the structure it once contaned. A few crates and chests remain relatively unharmed.'
r90d = 'The fancy designs have deteriorated a bit in the time between when they were carved and now, but most of their splendor remains. a circular table rests in the centre, and several small sections for a purpouse you cant see.'
r91d = 'The hallway has several other rooms that once connected to it, but they have all collapsed in on themselves. Some vines from the outside swamp have made it through the broken windows.'
r92d = 'The cushions and furniture are all ravaged, not fit for the luxurious lifestyle they once accomadated for. A solid iron vault door takes up lots of the western wall.'
r93d = 'A section that once contained all the valuable artifacts this area had to hold. Almost all the pedestals and storage crates have been looted, though upon inspection a long box has escaped notice.'
r94d = 'The area, while still hot and swampy, is calm and puts you at ease. This is one of the first areas youve found so far that you feel you would like to stay in. The hut is equiped with basic fishing gear, though nothing you can use.'
r95d = 'The storage shed has various items of use inside, they look fairly recently placed.'
r96d = 'Soft moss carpet lines the sides of the cave you walk along. The river flow provides a nice atmospheric noise, and the cave is lush and alive all around you.'
r97d = 'You can make out that the river flows even further down into the depths of the system. It isnt a good idea to jump off. You cant see the bottom, but similar wisps to the ones you saw at the bottom of the crossroads cavern dance around in the darkness.'
r98d = 'The oppressive swamp pushes in on you, the air taking on a more dangerous feel. You feel like you are being watched.'
r99d = 'The swamp water levels out, and you step onto rock. The swamp is unfriendly and chattering noises sound behind your back.'
r100d = 'The clearing is full of thick vines and ropy trees, knotted together forming walls around the glade. Gloom presses in, giving you paranoia and making you look over your shoulder for any other threats.'
r100trd = 'Entrance tunnel to the next cave system.'
r101d = 'An incessent dripping noise breaks the haunting silence that falls thick over the cave. A faint whistle that sounds like wind can be heard from further down.'
r102d = 'The smell of brine and salt is stronger here, barnacles and small crab shells littler the floors.'
r103d = 'The dock is made of what once would have been wood, but now is little more than a creaking, worn mass. The stone and metal are the only things holding it together.'
r104d = 'There is an area by which items would be loaded onto boats in days prior. its size surprises you; how much trade could these people get in a cave, you wonder. It appears that several cave entrances have collapsed since these people lived, leaving only scattered routes through which what was once a dense system.'
r105d = 'The item storage is quite small, as it is the only one that hasnt collapsed and is still explorable. Various crates lie with their contents still inside, but only one seems of real interest.'
r106d = 'The wooden docks continue on into the next larger cave, opening up onto a large lake.'
r107d = 'It only contains small fishing boats, but its all you need to be able to traverse the lakes.'
r108d = 'The lake is cold and the spray seeps into your bones. A current from some unknown point acts on the water.'
r109d = 'Some worn netting drifts around in the waters, eaten away at by the salt and time. Various spikes stick out of the water and reach up to the celing.'
r110d = 'The largest cave in the system that youve seen so far. Its scale mainly extends horizontally, with the far end being almost out of your vision, but the celing not reaching up to the higher levels. The creaking old galley moored in the middle next to an island is the main attraction.'
r111d = 'The rigging doesnt reach all the way up to the main deck, with the rips in the knots being to severe to use as handholds. The rigging is usable up to a hole in the gun deck.'
r112d = 'The deck is destroyed a fair bit, with rotting wood causing some and old battle scars the others. There are still some cannons that you can find, but there arent any canonballs left on deck.'
r113d = 'Storage is densely packed with crates, most of which contain nothing but rotted remains of food that make you pull back from the intense stench.'
r114d = 'What once would have been a fairly well furnished room has fallen into disrepair, the red drapings faded. There is surprisingly enough evidence that it had been stayed in recently, as some of the major holes have been patched up, and familiar maps left behind.'
r115d = 'The main deck is intact, though the wood looks as if it will give in under pressure. Brine and dust have built up on the deck, which seeps into the boards and make them creak.'
r116d = 'Fragile rigging still runs up to the little basket, giving you a good view of the whole area.'
r117d = 'The back deck is in similar condition to the rest of the ship. It is raised higher than the main deck.'
r118d = 'A little sandy shoreline, with some chests from the ship washed up on the shore. They look untouched.'
r119d = 'It is difficult to access the bay from the water, due to the jagged rocks that threaten to dash crafts on their harsh material. The spikes continue into the damp cave.'
r120d = 'The thread of water still runs through the centre of the passage, with the spiked rocks lining the outer sections.'
r121d = 'The structure is made of stone brick, and is mostly intact though the metal bars and defenses have eroded away over time. It has a haunting feel around it.'
r122d = 'A little side building which stores the weapons the post held. A few still remain inside.'
r123d = 'You gather that the many ships that were wrecked on the shores met with the hidden rocks underneath the waters. Their wood is rotten and they contain nothing of value.'
r124d = 'The gloom extends into this area, the passageway is concealed naturally so that it is difficult to see and fit through.'
r125d = 'The hut is made in a little hollow, and shielded well from everything outside. It looks like it was made relatively recently compared to everything else in the area.'
r126d = 'The spikes give way for the large, open space of water. The paddle of your boat seems small and insignificant compared to the rush of water currents and other eerie noises.'
r127d = ' -TO THE BLACK MINES- The winch lift has given out, though a ladder still remains to lower yourself down it. It looks like you will be able to get further towards the centre of the system as a whole through this mine.'
r128d = '128'
r129d = '129'
r130d = '130'
r131d = '131'
r132d = '132'
r133d = '133'
r134d = '134'
r135d = '135'
r136d = '136'
r137d = '137'
r138d = '138'
r139d = '139'
r140d = '140'
r141d = '141'
r142d = '142'
r143d = '143'
r144d = '144'
r145d = '145'
r146d = '146'
r147d = '147'
r148d = '148'
r149d = '149'
r150d = '150'
r151d = '151'
r152d = '152'
r153d = '153'
r154d = '154'
r155d = '155'
r156d = '156'
r157d = '157'
r158d = '158'
r159d = '159'
r160d = '160'
r161d = '161'
r162d = '162'
r163d = '163'
r164d = '164'
r165d = '165'
r166d = '166'
r167d = '167'
r168d = '168'




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
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
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

r66BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r71BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r68BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1 ,1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r75BM = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

r78BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1, 1],
         [1 ,1 ,1 ,1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r80BM = [[1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]]

r84BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r86BM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r91BM = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

r100BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r103BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1]]

r107BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r114BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r115BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r121BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

r126BM= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]






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
def astar(maze, start, end, enemy, type, enemy2, enemy3, enemy4):
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
    max_iterations = (len(maze[0]) * len(maze) //2 )
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
            if screen[enemy2.ETile]['x'] == node_position[1] and screen[enemy2.ETile]['y'] == node_position[0]:
              continue
          if type == 3:
            if screen[enemy2.ETile]['x'] == node_position[1] and screen[enemy2.ETile]['y'] == node_position[0]:
              continue
            if screen[enemy3.ETile]['x'] == node_position[1] and screen[enemy3.ETile]['y'] == node_position[0]:
              continue
          if type == 4:
            if screen[enemy2.ETile]['x'] == node_position[1] and screen[enemy2.ETile]['y'] == node_position[0]:
              continue
            if screen[enemy3.ETile]['x'] == node_position[1] and screen[enemy3.ETile]['y'] == node_position[0]:
              continue
            if screen[enemy4.ETile]['x'] == node_position[1] and screen[enemy4.ETile]['y'] == node_position[0]:
              continue


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


screen = {}

for i in range (400):
  screen[i] = {'num':0, 'display':'  ', 'x':0, 'y':0}

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
  def __init__(self,FType,ERoom,H,damage,defense,down,ETile,name,Ex,Ey,XP,ESpeed,DTXT,STile,WTimer):
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
    self.DTXT = DTXT
    self.STile = STile
    self.WTimer = WTimer


Enemy0A = E(2,r5,40,10,5,0,108,'Brute',1,1,10,3,False,310,0)
Enemy0B = E(2,r5,40,15,5,0,114,'Outcast',1,1,10,4,False,310,0)
Enemy1 = E(1,r24,100,25,10,0,50,'Gravedigger',1,1,30,2,False,370,0)
Enemy2A = E(2,r35,80,15,10,0,131,'Ash Wisp',1,1,20,5,False,190,0)
Enemy2B = E(2,r35,80,15,10,0,128,'Ash Wisp',1,1,20,5,False,190,0)
Enemy3A = E(2,r29,80,15,10,0,106,'Ash Wisp',1,1,20,5,False,218,0)
Enemy3B = E(2,r29,80,15,10,0,117,'Ash Wisp',1,1,20,5,False,218,0)
Enemy4 = E(1,r46,100,35,45,0,175,'Scorched Knight',1,1,50,3,False,190,0)
Enemy5 = E(1,r50,100,25,35,0,291,'Guard',1,1,35,5,False,185,0)
Enemy6 = E(1,r55,100,25,35,0,204,'Guard',1,1,35,5,False,197,0)
Sen1A =  E(4,r52,130,40,50,0,71,'Company Warden Kristoph',1,1,100,2,False,190,0)
Sen1B = E(4,r52,60,25,30,0,103,'Company Guard',1,1,35,3,False,197,0)
Sen1C = E(4,r52,60,25,30,0,136,'Company Guard',1,1,35,3,False,197,0)
Sen1D = E(4,r52,60,25,30,0,204,'Company Guard',1,1,35,3,False,197,0)
Enemy6 = E(1,r55,100,25,30,0,204,'Guard',1,1,35,5,False,197,0)
Enemy7 = E(1,r57,70,35,20,0,147,'Spiderling',1,1,35,8,False,213,0)
Enemy8 = E(1,r59,70,35,20,0,248,'Spiderling',1,1,35,8,False,252,0)
Sen2A =   E(3,r60,120,70,30,0,106,'King Arachnid',1,1,100,2,False,272,0)
Sen2B =   E(3,r60,70,40,30,0,75,'Giant Spider',1,1,100,5,False,272,0)
Sen2C =   E(3,r60,70,40,30,0,265,'Giant Spider',1,1,100,5,False,272,0)
Enemy9A = E(2,r66,80,40,30,0,86,'Shroomling',1,1,30,2,False,310,0)
Enemy9B = E(2,r66,80,40,30,0,153,'Shroomling',1,1,30,2,False,310,0)
Enemy10 = E(1,r71,130,50,20,0,266,'Pumpkin Hag',1,1,70,4,False,215,0)
Enemy11 = E(1,r68,1,1,99,0,253,'Hermit Greg',1,1,-1,0,False,208,0)
Enemy12A = E(3,r75,75,45,60,0,114,'Company Explorer',1,1,40,4,False,215,0)
Enemy12B = E(3,r75,75,45,60,0,189,'Company Explorer',1,1,40,4,False,215,0)
Enemy12C = E(3,r75,75,45,60,0,191,'Company Explorer',1,1,40,4,False,215,0)
Enemy13A = E(2,r78,60,50,5,0,133,'Cave Mite',1,1,40,6,False,206,0)
Enemy13B = E(2,r78,60,50,5,0,273,'Cave Mite',1,1,40,6,False,310,0)
Enemy14 = E(1,r80,150,45,50,0,29,'Winding Troll',1,1,70,4,False,367,0)
Enemy15 = E(1,r84,120,55,60,0,229,'M176-1R-G0L',1,1,60,2,False,111,0)
Enemy16A = E(3,r86,50,50,55,0,334,'Swamp Bug',1,1,50,5,False,331,0)
Enemy16B = E(3,r86,50,50,55,0,108,'Swamp Bug',1,1,50,5,False,331,0)
Enemy16C = E(3,r86,50,50,55,0,224,'Swamp Bug',1,1,50,5,False,331,0)
Enemy17A = E(2,r91,130,50,20,0,348,'Apparition Tank',1,1,80,2,False,30,0)
Enemy17B = E(2,r91,80,90,50,0,351,'Apparition Dagger',1,1,80,5,False,30,0)
Sen3A =   E(4,r100,150,75,45,0,217,'Swamp Thing',1,1,100,2,False,202,0)
Sen3B =   E(4,r100,60,60,30,0,211,'Vine Thrasher',1,1,100,0,False,202,0)
Sen3C =   E(4,r100,60,60,30,0,129,'Vine Thrasher',1,1,100,0,False,202,0)
Sen3D =   E(4,r100,60,60,30,0,249,'Vine Thrasher',1,1,100,0,False,202,0)
Enemy18A = E(3,r103,80,40,60,0,104,'Dockworker Ghost',1,1,40,4,False,218,0)
Enemy18B = E(3,r103,80,40,60,0,306,'Dockworker Ghost',1,1,40,4,False,218,0)
Enemy18C = E(3,r103,80,40,60,0,89,'Dockworker Ghost',1,1,40,4,False,218,0)
Enemy19 = E(1,r107,140,55,50,0,265,'Fisherman Ghoul',1,1,70,2,False,213,0)
Enemy20 = E(1,r114,150,65,30,0,105,'Phantom Captain',1,1,70,3,False,214,0)
Enemy21A = E(4,r115,90,50,60,0,128,'Phantom Pirate',1,1,40,3,False,211,0)
Enemy21B = E(4,r115,90,50,60,0,196,'Phantom Pirate',1,1,40,3,False,211,0)
Enemy21C = E(4,r115,90,50,60,0,203,'Phantom Pirate',1,1,40,3,False,211,0)
Enemy21D = E(4,r115,90,50,60,0,268,'Phantom Pirate',1,1,40,3,False,211,0)
Enemy22A = E(3,r121,80,40,60,0,252,'Dockworker Ghost',1,1,40,4,False,205,0)
Enemy22B = E(3,r121,80,40,60,0,265,'Dockworker Ghost',1,1,40,4,False,205,0)
Enemy22C = E(3,r121,80,40,60,0,111,'Dockworker Ghost',1,1,40,4,False,205,0)
Sen4A =   E(4,r126,180,50,40,0,216,'Kraken',1,1,100,0,False,202,0)
Sen4B =   E(4,r126,100,70,30,0,175,'Tentacle',1,1,100,5,False,202,0)
Sen4C =   E(4,r126,100,70,30,0,214,'Tentacle',1,1,100,5,False,202,0)
Sen4D =   E(4,r126,100,70,30,0,255,'Tentacle',1,1,100,5,False,22,0)


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
  print("    "+rooms[r13]['mmc']+"|   |"+connect[16]['display']+"--"+rooms[r14]['mmc']+"|   |"+Fore.RESET+" "+connect[18]['display']+"...              ")
  print("     "+rooms[r13]['mmc']+"---    "+rooms[r14]['mmc']+"- - "+Fore.RESET+"                    ")
  print("      "+connect[15]['display']+"|     "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"                 ")
  print("      "+connect[15]['display']+"|     "+rooms[r10]['mmc']+"[ ]                 ")
  print("     "+rooms[r12]['mmc']+"----   "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"       "+connect[19]['display']+":              ")
  print("    "+rooms[r12]['mmc']+"|    |  "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+"       "+connect[19]['display']+":              ")
  print("     "+rooms[r12]['mmc']+"----   "+rooms[r10]['mmc']+"[ ]   "+rooms[r5]['mmc']+"----------"+Fore.RESET+"              ")
  print("       "+connect[14]['display']+"|    "+rooms[r10]['mmc']+"[ ]   "+rooms[r5]['mmc']+"|        |"+Fore.RESET+""+connect[11]['display']+"---"+rooms[r6]['mmc']+"[ ]"+Fore.RESET+""+connect[9]['display']+"--"+rooms[r7]['mmc']+"[___]              ")
  print("      "+rooms[r11]['mmc']+"[ ]"+Fore.RESET+""+connect[13]['display']+"---"+rooms[r10]['mmc']+"[ ]   "+rooms[r5]['mmc']+"|        |"+Fore.RESET+"    "+connect[10]['display']+"|     "+connect[8]['display']+"|              ")
  print("            "+rooms[r10]['mmc']+"[ ]"+Fore.RESET+""+connect[12]['display']+"---"+rooms[r5]['mmc']+"|        |  "+rooms[r9]['mmc']+"[___]  "+rooms[r8]['mmc']+"[ ]"+Fore.RESET+"              ")
  print("             "+connect[7]['display']+"|    "+rooms[r5]['mmc']+"---------- "+Fore.RESET+"         "+connect[6]['display']+"|              ")
  print("             "+connect[7]['display']+"|        "+connect[5]['display']+"|               "+connect[6]['display']+"|              ")
  print("             "+connect[7]['display']+"|      "+rooms[r2]['mmc']+"----- "+Fore.RESET+"            "+connect[6]['display']+"|              ")
  print("            "+rooms[r4]['mmc']+"[  ]"+Fore.RESET+""+connect[3]['display']+"----"+rooms[r2]['mmc']+"|   |"+Fore.RESET+""+connect[2]['display']+"---"+rooms[r1]['mmc']+"[ ]"+Fore.RESET+""+connect[4]['display']+"------"+rooms[r3]['mmc']+"[ ]              ")
  print("            "+rooms[r4]['mmc']+"[  ]    "+rooms[r2]['mmc']+"|   |"+Fore.RESET+"    "+connect[1]['display']+"|              ")
  print("                    "+rooms[r2]['mmc']+"-----   "+rooms[r0]['mmc']+"[ ]<--- Start              ")


def crypts():
  print(""+Fore.RESET+"       "+rooms[r15]['mmc']+" -----    "+rooms[r18]['mmc']+" ----------  "+rooms[r20]['mmc']+" ----------                   ")
  print("       "+rooms[r15]['mmc']+"|     |   "+rooms[r18]['mmc']+"|          | "+rooms[r20]['mmc']+"|          |"+Fore.RESET+""+connect[29]['display']+"----+                 ")      
  print("    "+connect[18]['display']+"..."+rooms[r15]['mmc']+"|     |    "+rooms[r18]['mmc']+"----------   "+rooms[r20]['mmc']+"----------"+Fore.RESET+"     "+connect[29]['display']+"|                 ")
  print("        "+rooms[r15]['mmc']+"-----"+Fore.RESET+"            "+connect[22]['display']+"|      "+connect[28]['display']+"|    "+rooms[r24]['mmc']+"-------------------- "+Fore.RESET+"                ")
  print("          "+connect[20]['display']+"|       "+rooms[r17]['mmc']+"---------"+Fore.RESET+"     "+connect[28]['display']+"|   "+rooms[r24]['mmc']+"|                    |"+Fore.RESET+""+connect[30]['display']+"--"+rooms[r25]['mmc']+"[ ]"+connect[31]['display']+"....                 ")
  print("       "+rooms[r16]['mmc']+" -----    "+rooms[r17]['mmc']+"|         |"+Fore.RESET+"    "+connect[28]['display']+"|   "+rooms[r24]['mmc']+"|                    |                 ")
  print("       "+rooms[r16]['mmc']+"|     |"+connect[21]['display']+"---"+rooms[r17]['mmc']+"|         |"+Fore.RESET+""+connect[23]['display']+"---"+rooms[r19]['mmc']+"[ ]   "+rooms[r24]['mmc']+"--------------------                 ")
  print("       "+rooms[r16]['mmc']+"|     |   "+rooms[r17]['mmc']+"|         |"+Fore.RESET+"    "+connect[24]['display']+"|     "+connect[27]['display']+"|                 ")
  print("        "+rooms[r16]['mmc']+"-----     "+rooms[r17]['mmc']+"---------    "+rooms[r21]['mmc']+"[ ]"+Fore.RESET+""+connect[25]['display']+"--"+rooms[r23]['mmc']+"[   ]"+Fore.RESET+"                 ")
  print("          "+connect[19]['display']+":                           "+connect[26]['display']+"|                 ")
  print("          "+connect[19]['display']+":                         "+rooms[r22]['mmc']+" ---                 ")
  print("                                    "+rooms[r22]['mmc']+"|   |                 ")
  print("                                     "+rooms[r22]['mmc']+"---                 ")


def wastes():
  print(""+Fore.RESET+"                              "+connect[46]['display']+"...."+rooms[r39]['mmc']+"[ ] "+Fore.RESET+"             ")
  print("                                   "+connect[45]['display']+"|               ")
  print("          "+connect[51]['display']+":                       "+rooms[r38]['mmc']+"-- "+Fore.RESET+"              ")
  print("          "+connect[51]['display']+":         "+connect[47]['display']+":            "+rooms[r38]['mmc']+"|  | "+Fore.RESET+"             ")
  print("        "+rooms[r31]['mmc']+" -- "+connect[47]['display']+"        :      "+rooms[r34]['mmc']+"---   "+rooms[r38]['mmc']+"|  |"+Fore.RESET+"              ")
  print("  "+rooms[r30]['mmc']+"[ ]"+connect[36]['display']+"---"+rooms[r31]['mmc']+"|  |"+connect[37]['display']+"--"+rooms[r32]['mmc']+"[ ]"+connect[38]['display']+"--"+rooms[r33]['mmc']+"[ ]"+connect[39]['display']+"----"+rooms[r34]['mmc']+"|   |  "+rooms[r38]['mmc']+"|  | "+Fore.RESET+"             ")
  print("   "+connect[35]['display']+"|     "+rooms[r31]['mmc']+"--                "+rooms[r34]['mmc']+"---   "+rooms[r38]['mmc']+"|  |"+Fore.RESET+"              ")
  print("   "+connect[35]['display']+"|      "+connect[183]['display']+"|                 "+connect[40]['display']+"|    "+rooms[r38]['mmc']+" --"+Fore.RESET+"               ")
  print(""+rooms[r29]['mmc']+" ------  "+rooms[r40]['mmc']+"[  ]    "+rooms[r27]['mmc']+"----"+Fore.RESET+"       "+connect[40]['display']+"|     "+connect[44]['display']+"|                ")
  print(""+rooms[r29]['mmc']+"|      |        "+rooms[r27]['mmc']+"|    |"+connect[41]['display']+"-----"+rooms[r35]['mmc']+"[ ]"+connect[42]['display']+"---"+rooms[r36]['mmc']+"[ ]               ")
  print(""+rooms[r29]['mmc']+"|      |"+connect[34]['display']+"---"+rooms[r28]['mmc']+"[ ]"+connect[33]['display']+"--"+rooms[r27]['mmc']+"|    |"+connect[43]['display']+"            |                ")
  print(""+rooms[r29]['mmc']+"|      |        "+rooms[r27]['mmc']+" ----          "+rooms[r37]['mmc']+" -----              ")
  print(" "+rooms[r29]['mmc']+"------ "+Fore.RESET+"          "+connect[32]['display']+"|            "+rooms[r37]['mmc']+"|     |             ")
  print("                 "+rooms[r26]['mmc']+"[ ]           "+rooms[r37]['mmc']+" -----              ")
  print("                  "+connect[31]['display']+":")
  print("                  "+connect[31]['display']+":") 

def deltas():
  print("          "+connect[63]['display']+"...."+rooms[r46]['mmc']+"[ ]"+connect[54]['display']+"....                        ")
  print("               "+connect[53]['display']+"|                     ")
  print("             "+rooms[r44]['mmc']+" ---                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |                  ")
  print("             "+rooms[r44]['mmc']+"|   |             "+rooms[r45]['mmc']+"[ ]                  ")
  print("             "+rooms[r44]['mmc']+"|   |"+connect[48]['display']+"              |                  ")
  print("             "+rooms[r44]['mmc']+" ---         "+rooms[r41]['mmc']+"------------"+Fore.RESET+"                  ")
  print("               "+connect[52]['display']+"|         "+rooms[r41]['mmc']+"|            |                  ")
  print("            "+rooms[r42]['mmc']+"------       "+rooms[r41]['mmc']+"|            |                  ")
  print("    "+rooms[r43]['mmc']+" --    "+rooms[r42]['mmc']+"|      |      "+rooms[r41]['mmc']+"|            |                  ")
  print("    "+rooms[r43]['mmc']+"|  |"+connect[50]['display']+"---"+rooms[r42]['mmc']+"|      |"+connect[49]['display']+"------"+rooms[r41]['mmc']+"|            | "+connect[46]['display']+".....            ")
  print("     "+rooms[r43]['mmc']+"--    "+rooms[r42]['mmc']+" ------       "+rooms[r41]['mmc']+"|            | "+Fore.RESET+"                 ")
  print("     "+connect[51]['display']+":                   "+rooms[r41]['mmc']+" ------------ "+Fore.RESET+"                 ")
  print("     "+connect[51]['display']+":                         "+connect[47]['display']+":                  ")
  print("     "+connect[51]['display']+":                         "+connect[47]['display']+":                  ")


def lockhouse():
  print('                       '+connect[84]['display']+':       ')
  print('                       '+connect[84]['display']+':     ')
  print('                      '+rooms[r54]['mmc']+'[ ]     ')
  print('    '+rooms[r55]['mmc']+'------------       '+connect[62]['display']+'|    '+rooms[r52]['mmc']+'-------     ')
  print('   '+rooms[r55]['mmc']+'|            |     '+rooms[r53]['mmc']+'[ ]'+connect[61]['display']+'--'+rooms[r52]['mmc']+'|       |'+Fore.RESET+'     ')
  print('    '+rooms[r55]['mmc']+'------------           '+rooms[r52]['mmc']+'|       | '+Fore.RESET+'     ')
  print('        '+connect[55]['display']+'|                   '+rooms[r52]['mmc']+'-------'+Fore.RESET+'     ')
  print('      '+rooms[r47]['mmc']+'--------                '+connect[60]['display']+'|     ')
  print('     '+rooms[r47]['mmc']+'|        |               '+connect[60]['display']+'|     ')
  print(' '+connect[54]['display']+'....'+rooms[r47]['mmc']+'|        |'+connect[57]['display']+'----'+rooms[r50]['mmc']+'[ ]      '+rooms[r51]['mmc']+'-----     ')
  print('     '+rooms[r47]['mmc']+'|        |'+connect[58]['display']+'     |      '+rooms[r51]['mmc']+'|     |     ')
  print('     '+rooms[r47]['mmc']+' --------     '+rooms[r49]['mmc']+'[ ]'+connect[59]['display']+'-----'+rooms[r51]['mmc']+'|     |'+Fore.RESET+'     ')
  print('          '+connect[56]['display']+'|                 '+rooms[r51]['mmc']+'-----'+Fore.RESET+'     ')
  print('        '+rooms[r48]['mmc']+'[   ]     ')


def spiders():
   print('     '+connect[71]['display']+':          ')
   print('     '+connect[71]['display']+':          ')
   print('    '+rooms[r62]['mmc']+'---          ')
   print('   '+rooms[r62]['mmc']+'|   |          ')
   print('    '+rooms[r62]['mmc']+'---'+Fore.RESET+'          ')
   print('     '+connect[70]['display']+'|          ')
   print('   '+rooms[r60]['mmc']+'-----     '+rooms[r59]['mmc']+'---          ')
   print('  '+rooms[r60]['mmc']+'|     |'+connect[69]['display']+'---'+rooms[r59]['mmc']+'|   |          ')
   print('  '+rooms[r60]['mmc']+'|     |    '+rooms[r59]['mmc']+'---          ')
   print('   '+rooms[r60]['mmc']+'-----      '+connect[68]['display']+'|          ')
   print('     '+connect[67]['display']+'|      '+rooms[r56]['mmc']+'--------          ')
   print('    '+rooms[r61]['mmc']+'---    '+rooms[r56]['mmc']+'|        |          ')
   print('   '+rooms[r61]['mmc']+'|   |'+connect[66]['display']+'---'+rooms[r56]['mmc']+'|        |'+connect[63]['display']+'....          ')
   print('    '+rooms[r61]['mmc']+'---    '+rooms[r56]['mmc']+'|        |          ')
   print('            '+rooms[r56]['mmc']+'--------'+Fore.RESET+'          ')
   print('               '+connect[64]['display']+'|           ')
   print('              '+rooms[r57]['mmc']+'[ ]'+Fore.RESET+'          ')
   print('               '+connect[65]['display']+'|          ')
   print('             '+rooms[r58]['mmc']+'[   ]          ')


def shrooms():
  print(''+Fore.RESET+'               '+rooms[r70]['mmc']+'[ ]                                ')
  print('      '+rooms[r71]['mmc']+'-----     '+connect[76]['display']+'|                                         ')
  print('     '+rooms[r71]['mmc']+'|     |   '+rooms[r69]['mmc']+'---                                       ')
  print('     '+rooms[r71]['mmc']+'|     |'+connect[77]['display']+'--'+rooms[r69]['mmc']+'|   |        '+rooms[r72]['mmc']+'---                               ')
  print('      '+rooms[r71]['mmc']+'-----    '+rooms[r69]['mmc']+'---        '+rooms[r72]['mmc']+'|   |'+connect[81]['display']+'...                    ')
  print('                '+connect[75]['display']+'|          '+rooms[r72]['mmc']+'---                                            ')
  print('            '+rooms[r66]['mmc']+'----------      '+connect[79]['display']+'|                                             ')
  print('           '+rooms[r66]['mmc']+'|          |    '+rooms[r67]['mmc']+'---                                               ')
  print('           '+rooms[r66]['mmc']+'|          |'+connect[78]['display']+'---'+rooms[r67]['mmc']+'|   |'+connect[80]['display']+'--'+rooms[r68]['mmc']+'[ ]                                ')
  print('           '+rooms[r66]['mmc']+'|          |    '+rooms[r67]['mmc']+'---                                             ')
  print('           '+rooms[r66]['mmc']+'|          |                                                   ')
  print('            '+rooms[r66]['mmc']+'----------                                             ')
  print('                '+connect[74]['display']+'|                                                 ')
  print('       '+rooms[r63]['mmc']+'---     '+rooms[r64]['mmc']+'---     '+rooms[r65]['mmc']+'---                                           ')
  print('      '+rooms[r63]['mmc']+'|   |'+connect[72]['display']+'---'+rooms[r64]['mmc']+'|   |'+connect[73]['display']+'---'+rooms[r65]['mmc']+'|   |                                  ')
  print('       '+rooms[r63]['mmc']+'---     '+rooms[r64]['mmc']+'---     '+rooms[r65]['mmc']+'---                          ')
  print('        '+connect[71]['display']+':                                                             ')
  print('        '+connect[71]['display']+':                                        ')


def caves():
  print('             '+rooms[r82]['mmc']+'---               ')
  print('            '+rooms[r82]['mmc']+'|   |'+connect[92]['display']+'---'+rooms[r83]['mmc']+'[ ]                ')
  print('             '+rooms[r82]['mmc']+'---     '+connect[93]['display']+'|        ')
  print('              '+connect[91]['display']+'|     '+rooms[r84]['mmc']+'---      ')
  print('             '+rooms[r81]['mmc']+'---   '+rooms[r84]['mmc']+'|   |       ')
  print('         '+connect[94]['display']+'...'+rooms[r81]['mmc']+'|   |   '+rooms[r84]['mmc']+'---      ')
  print('             '+rooms[r81]['mmc']+'---            ')
  print('              '+connect[90]['display']+'|                   ')
  print('             '+rooms[r80]['mmc']+'---                ')
  print('            '+rooms[r80]['mmc']+'|   |            ')
  print('            '+rooms[r80]['mmc']+'|   |          ')
  print('            '+rooms[r80]['mmc']+'|   |           ')
  print('            '+rooms[r80]['mmc']+'|   |            ')
  print('     '+rooms[r77]['mmc']+'[ ]'+connect[86]['display']+'----'+rooms[r80]['mmc']+'|   |              ')
  print('      '+connect[85]['display']+'|      '+rooms[r80]['mmc']+'---               ')
  print('      '+connect[85]['display']+'|       '+connect[89]['display']+'|                ')
  print('   '+rooms[r76]['mmc']+'-----     '+rooms[r78]['mmc']+'---                ')
  print('  '+rooms[r76]['mmc']+'|     |'+connect[87]['display']+'---'+rooms[r78]['mmc']+'|   |'+connect[88]['display']+'---'+rooms[r79]['mmc']+'[ ]             ')
  print('  '+rooms[r76]['mmc']+'|     |    '+rooms[r78]['mmc']+'---                  ')
  print('   '+rooms[r76]['mmc']+'-----                         ')
  print('     '+connect[84]['display']+':                               ')
  print('     '+connect[84]['display']+':                     ')


def mists():
  print('       '+connect[105]['display']+':                                    ')
  print('       '+connect[105]['display']+':                                    ')
  print('     '+rooms[r86]['mmc']+'-----   '+rooms[r89]['mmc']+'[ ]                                    ')
  print(' '+connect[101]['display']+'...'+rooms[r86]['mmc']+'|     |   '+connect[99]['display']+'|    '+rooms[r88]['mmc']+'---                          ')
  print('    '+rooms[r86]['mmc']+'|     |'+connect[100]['display']+'--'+rooms[r87]['mmc']+'[ ]'+connect[98]['display']+'--'+rooms[r88]['mmc']+'|   |                                ')
  print('     '+rooms[r86]['mmc']+'-----         '+rooms[r88]['mmc']+'---                        ')
  print('      '+connect[96]['display']+'|             '+connect[97]['display']+'|                       ')
  print('   '+rooms[r85]['mmc']+'-----    '+rooms[r75]['mmc']+'-----------------             ')
  print('  '+rooms[r85]['mmc']+'|     |  '+rooms[r75]['mmc']+'|                 |               ')
  print('  '+rooms[r85]['mmc']+'|     |'+connect[95]['display']+'--'+rooms[r75]['mmc']+'|                 |               ')
  print('   '+rooms[r85]['mmc']+'-----   '+rooms[r75]['mmc']+'|                 |               ')
  print('           '+rooms[r75]['mmc']+'|                 |'+connect[94]['display']+'....          ')
  print('           '+rooms[r75]['mmc']+'|                 |               ')
  print('           '+rooms[r75]['mmc']+'|                 |               ')
  print('           '+rooms[r75]['mmc']+'|                 |               ')
  print('            '+rooms[r75]['mmc']+'-----------------               ')
  print('              '+rooms[r73]['mmc']+'---    '+connect[83]['display']+'|                       ')
  print('          '+connect[81]['display']+'...'+rooms[r73]['mmc']+'|   |'+connect[82]['display']+'--'+rooms[r74]['mmc']+'[ ]                       ')
  print('              '+rooms[r73]['mmc']+'---                           ')
  print('                                            ')


def parlour():
  print(''+Fore.RESET+'        '+rooms[r90]['mmc']+'--------       ')
  print('       '+rooms[r90]['mmc']+'|        |      ')
  print('       '+rooms[r90]['mmc']+'|        |'+connect[101]['display']+'....  ')
  print('       '+rooms[r90]['mmc']+'|        |      ')
  print('        '+rooms[r90]['mmc']+'--------       ')
  print('            '+connect[102]['display']+'|          ')
  print('           '+rooms[r91]['mmc']+'---         ')
  print('          '+rooms[r91]['mmc']+'|   |         ')
  print('          '+rooms[r91]['mmc']+'|   |        ')
  print('          '+rooms[r91]['mmc']+'|   |        ')
  print('           '+rooms[r91]['mmc']+'---         ')
  print('            '+connect[103]['display']+'|          ')
  print('    '+rooms[r93]['mmc']+'---    '+rooms[r92]['mmc']+'---         ')
  print('   '+rooms[r93]['mmc']+'|   |'+connect[104]['display']+'--'+rooms[r92]['mmc']+'|   |        ')
  print('    '+rooms[r93]['mmc']+'---    '+rooms[r92]['mmc']+'---         ')


def river():
  print('  '+rooms[r95]['mmc']+'[ ]              ')
  print('   '+connect[106]['display']+'|              ')
  print('  '+rooms[r94]['mmc']+'---     '+rooms[r96]['mmc']+'--------------    '+rooms[r97]['mmc']+'---       ')
  print(' '+rooms[r94]['mmc']+'|   |'+connect[107]['display']+'---'+rooms[r96]['mmc']+'|              |'+connect[108]['display']+'--'+rooms[r97]['mmc']+'|   |        ')
  print('  '+rooms[r94]['mmc']+'---     '+rooms[r96]['mmc']+'--------------    '+rooms[r97]['mmc']+'---          ')
  print('   '+connect[105]['display']+':                         '+connect[109]['display']+'|            ')
  print('   '+connect[105]['display']+':                   '+rooms[r99]['mmc']+'[ ]'+connect[110]['display']+'--'+rooms[r98]['mmc']+'[ ]           ')
  print('                        '+connect[111]['display']+'|                  ')
  print('                      '+rooms[r100]['mmc']+'------------         ')
  print('                     '+rooms[r100]['mmc']+'|            |'+connect[112]['display']+'--'+rooms[r100tr]['mmc']+'[ ]'+connect[113]['display']+'...    ')
  print('                      '+rooms[r100]['mmc']+'------------        ')


def lakes():
  print('                                   '+connect[122]['display']+':              ')
  print('                                   '+connect[122]['display']+':              ')
  print('                         '+rooms[r108]['mmc']+'--------------------     ')
  print('                        '+rooms[r108]['mmc']+'|                    |    ')
  print('                        '+rooms[r108]['mmc']+'|                    |    ')
  print('  '+rooms[r107]['mmc']+'---     '+rooms[r106]['mmc']+'-------       '+rooms[r108]['mmc']+'|                    |'+connect[135]['display']+'....')
  print(' '+rooms[r107]['mmc']+'|   |   '+rooms[r106]['mmc']+'|       |      '+rooms[r108]['mmc']+'|                    |    ')
  print(' '+rooms[r107]['mmc']+'|   |'+connect[120]['display']+'---'+rooms[r106]['mmc']+'|       |'+connect[121]['display']+'------'+rooms[r108]['mmc']+'|                    |    ')
  print(' '+rooms[r107]['mmc']+'|   |   '+rooms[r106]['mmc']+'|       |      '+rooms[r108]['mmc']+'|                    |    ')
  print('  '+rooms[r107]['mmc']+'---     '+rooms[r106]['mmc']+'-------        '+rooms[r108]['mmc']+'--------------------     ')
  print('             '+connect[118]['display']+'|           '+connect[115]['display']+'|                                              ')
  print('             '+connect[118]['display']+'|         '+rooms[r102]['mmc']+'---                        ')
  print('            '+rooms[r104]['mmc']+'[ ]'+connect[117]['display']+'--'+rooms[r103]['mmc']+'[ ]'+connect[116]['display']+'--'+rooms[r102]['mmc']+'|   |                       ')
  print('             '+connect[119]['display']+'|         '+rooms[r102]['mmc']+'---                        ')
  print('           '+rooms[r105]['mmc']+'-----       '+connect[114]['display']+' |                          ')
  print('          '+rooms[r105]['mmc']+'|     |      '+rooms[r101]['mmc']+'---                        ')
  print('           '+rooms[r105]['mmc']+'-----      '+rooms[r101]['mmc']+'|   |                       ')
  print('                      '+rooms[r101]['mmc']+' ---                        ')
  print('                        '+connect[113]['display']+':                         ')
  print('                        '+connect[113]['display']+':                         ')


def ship():
  print('               '+rooms[r110]['mmc']+' -------------------------------------------  ')
  print('               '+rooms[r110]['mmc']+'|                     '+rooms[r116]['mmc']+'[ ]                   '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|                      '+connect[127]['display']+'|                    '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|        '+rooms[r117]['mmc']+'-----    '+rooms[r115]['mmc']+'---------                 '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|       '+rooms[r117]['mmc']+'|     |'+connect[128]['display']+'--'+rooms[r115]['mmc']+'|         |                '+rooms[r110]['mmc']+'| ')
  print('  '+rooms[r118]['mmc']+'-------      '+rooms[r110]['mmc']+'|       '+rooms[r117]['mmc']+'|     |   '+rooms[r115]['mmc']+'---------                 '+rooms[r110]['mmc']+'| ')
  print(' '+rooms[r118]['mmc']+'|       |     '+rooms[r110]['mmc']+'|        '+rooms[r117]['mmc']+'-----        '+connect[124]['display']+'|                     '+rooms[r110]['mmc']+'| ')
  print(' '+rooms[r118]['mmc']+'|       |'+connect[129]['display']+'-----'+rooms[r110]['mmc']+'|          '+rooms[r114]['mmc']+'---    '+rooms[r112]['mmc']+'---------     '+rooms[r113]['mmc']+'-----       '+rooms[r110]['mmc']+'| ')
  print(' '+rooms[r118]['mmc']+'|       |     '+rooms[r110]['mmc']+'|         '+rooms[r114]['mmc']+'|   |'+connect[126]['display']+'--'+rooms[r112]['mmc']+'|         |'+connect[125]['display']+'---'+rooms[r113]['mmc']+'|     |      '+rooms[r110]['mmc']+'| ')
  print('  '+rooms[r118]['mmc']+'-------      '+rooms[r110]['mmc']+'|          '+rooms[r114]['mmc']+'---    '+rooms[r112]['mmc']+'---------     '+rooms[r113]['mmc']+'-----       '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|                     '+connect[123]['display']+'|                     '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|                    '+rooms[r111]['mmc']+'[ ]                    '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|                     '+connect[141]['display']+'|                     '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|                     '+connect[141]['display']+':                     '+rooms[r110]['mmc']+'| ')
  print('               '+rooms[r110]['mmc']+'|                                           | ')
  print('                '+rooms[r110]['mmc']+'-------------------------------------------  ')
  print('                                  '+connect[122]['display']+':                          ')
  print('                                  '+connect[122]['display']+':                          ')


def hold():
  print('       '+rooms[r119]['mmc']+'---      '+rooms[r121]['mmc']+' -----                             ')
  print('   '+connect[130]['display']+'...'+rooms[r119]['mmc']+'|   |'+connect[133]['display']+'-----'+rooms[r121]['mmc']+'|     |                            ')
  print('       '+rooms[r119]['mmc']+'---      '+rooms[r121]['mmc']+'|     |                            ')
  print('        '+connect[131]['display']+'|        '+rooms[r121]['mmc']+'-----                             ')
  print('       '+rooms[r120]['mmc']+'[ ]         '+connect[134]['display']+'|                               ')
  print('        '+connect[132]['display']+'|         '+rooms[r122]['mmc']+'[ ]                              ')
  print('    '+rooms[r109]['mmc']+'--------      '+rooms[r126]['mmc']+'--------     '+rooms[r127]['mmc']+'--------            ')
  print('   '+rooms[r109]['mmc']+'|        |    '+rooms[r126]['mmc']+'|        |   '+rooms[r127]['mmc']+'|        |           ')
  print(''+connect[135]['display']+'...'+rooms[r109]['mmc']+'|        |'+connect[139]['display']+'----'+rooms[r126]['mmc']+'|        |'+connect[140]['display']+'---'+rooms[r127]['mmc']+'|        | '+connect[141]['display']+'--> descend       ')
  print('   '+rooms[r109]['mmc']+'|        |    '+rooms[r126]['mmc']+'|        |   '+rooms[r127]['mmc']+'|        |           ')
  print('    '+rooms[r109]['mmc']+'--------      '+rooms[r126]['mmc']+'--------     '+rooms[r127]['mmc']+'--------            ')
  print('        '+connect[136]['display']+'|                                          ')
  print('      '+rooms[r123]['mmc']+'-----      '+rooms[r124]['mmc']+'---    '+rooms[r125]['mmc']+'------                     ')
  print('     '+rooms[r123]['mmc']+'|     |'+connect[137]['display']+'----'+rooms[r124]['mmc']+'|   |'+connect[138]['display']+'--'+rooms[r125]['mmc']+'|      |                    ')
  print('      '+rooms[r123]['mmc']+'-----      '+rooms[r124]['mmc']+'---    '+rooms[r125]['mmc']+'------                     ')


def haunt():
  print('                                        '+rooms[r142]['mmc']+'-----------------                                   ')
  print('                      '+rooms[r144]['mmc']+'-------          '+rooms[r142]['mmc']+'|                 |'+connect[157]['display']+'--'+rooms[r143]['mmc']+'[ ]                             ')
  print('                  '+connect[159]['display']+'...'+rooms[r144]['mmc']+'|       |          '+rooms[r142]['mmc']+'-----------------                                   ')
  print('                     '+rooms[r144]['mmc']+'|       |           '+connect[156]['display']+'|                                                  ')
  print('              '+rooms[r131]['mmc']+'[ ]     '+rooms[r144]['mmc']+'-------           '+rooms[r141]['mmc']+'---    '+rooms[r138]['mmc']+'--------------                               ')
  print('               '+connect[144]['display']+'|         '+connect[158]['display']+'|     '+rooms[r140]['mmc']+'[ ]'+connect[155]['display']+'-----'+rooms[r141]['mmc']+'|   |  '+rooms[r138]['mmc']+'/              \                              ')
  print('            '+rooms[r130]['mmc']+'-------    '+rooms[r132]['mmc']+'-----    '+connect[154]['display']+'|       '+rooms[r141]['mmc']+'---  '+rooms[r138]['mmc']+'/                \                             ')
  print('           '+rooms[r130]['mmc']+'|       |'+connect[145]['display']+'--'+rooms[r132]['mmc']+'|     |   '+connect[154]['display']+'|           '+rooms[r138]['mmc']+'/                  \                            ')
  print('            '+rooms[r130]['mmc']+'-------   '+rooms[r132]['mmc']+'|     |  '+rooms[r139]['mmc']+'[ ]'+connect[153]['display']+'--'+rooms[r137]['mmc']+'[ ]'+connect[152]['display']+'--'+rooms[r138]['mmc']+'[ :                    |                           ')
  print('            '+connect[143]['display']+'|         '+rooms[r132]['mmc']+'|     |        '+connect[151]['display']+'|     '+rooms[r138]['mmc']+'|                    |                           ')
  print('           '+rooms[r129]['mmc']+'[ ]        '+rooms[r132]['mmc']+'|     |'+connect[149]['display']+'--'+rooms[r135]['mmc']+'[ ]'+connect[150]['display']+'--'+rooms[r136]['mmc']+'[ ]    '+rooms[r138]['mmc']+'|                    |                           ')
  print('            '+connect[142]['display']+'|          '+rooms[r132]['mmc']+'-----    '+connect[148]['display']+'|          '+rooms[r138]['mmc']+'|                    |                           ')
  print('         '+rooms[r128]['mmc']+'------          '+rooms[r134]['mmc']+'----------      '+rooms[r138]['mmc']+' /                     |                           ')
  print('        '+rooms[r128]['mmc']+'|      |'+connect[146]['display']+'---'+rooms[r133]['mmc']+'[ ]'+connect[147]['display']+'--'+rooms[r134]['mmc']+'|          |     '+rooms[r138]['mmc']+'/                      |                           ')
  print('    '+connect[141]['display']+'<---'+rooms[r128]['mmc']+'|      |        '+rooms[r134]['mmc']+'|          |    '+rooms[r138]['mmc']+'|                       /                           ')
  print(' '+connect[141]['display']+'ascend  '+rooms[r128]['mmc']+'------         '+rooms[r134]['mmc']+'|          |    '+rooms[r138]['mmc']+'|                      /                            ')
  print('                        '+rooms[r134]['mmc']+'|          |    '+rooms[r138]['mmc']+'\                     /                             ')
  print('                         '+rooms[r134]['mmc']+'----------      '+rooms[r138]['mmc']+'---------------------                              ')


def wisp():
  print('                                        '+rooms[r150]['mmc']+'------------                      ')
  print('                                       '+rooms[r150]['mmc']+'|            |                     ')
  print('                                       '+rooms[r150]['mmc']+'|            |                     ')
  print('                          '+rooms[r147]['mmc']+'-----        '+rooms[r150]['mmc']+'|            |                     ')
  print('                         '+rooms[r147]['mmc']+'|     |'+connect[163]['display']+'--'+rooms[r149]['mmc']+'[ ]'+connect[164]['display']+'--'+rooms[r150]['mmc']+'|            |            '+connect[172]['display']+':        ')
  print('                         '+rooms[r147]['mmc']+'|     |        '+rooms[r150]['mmc']+'------------             '+connect[172]['display']+':        ')
  print('                  '+rooms[r146]['mmc']+'[ ]'+connect[161]['display']+'----'+rooms[r147]['mmc']+'|     |                 '+connect[165]['display']+'|     '+rooms[r154]['mmc']+'------------       ')
  print('                   '+connect[160]['display']+'|      '+rooms[r147]['mmc']+'-----           '+rooms[r151]['mmc']+'[ ]'+connect[166]['display']+'--'+rooms[r152]['mmc']+'[   ]'+connect[168]['display']+'--'+rooms[r154]['mmc']+'|            |      ')
  print('             '+rooms[r145]['mmc']+'---------       '+connect[162]['display']+'|                   '+connect[167]['display']+'|     '+rooms[r154]['mmc']+'------------       ')
  print('            '+rooms[r145]['mmc']+'|         |     '+rooms[r148]['mmc']+'[ ]                 '+rooms[r153]['mmc']+'[ ]             '+connect[169]['display']+'|    '+rooms[r157]['mmc']+'---  ')
  print('            '+rooms[r145]['mmc']+'|         |'+connect[159]['display']+'....                               '+rooms[r156]['mmc']+'[ ]'+connect[170]['display']+'--'+rooms[r155]['mmc']+'[ ]'+connect[171]['display']+'--'+rooms[r157]['mmc']+'|   | ')
  print('            '+rooms[r145]['mmc']+'|         |                                              '+rooms[r157]['mmc']+'---  ')
  print('             '+rooms[r145]['mmc']+'---------                                                    ')


def dark():
  print('                  '+rooms[r165]['mmc']+'---------                                          ')
  print('                 '+rooms[r165]['mmc']+'|         |                                         ')
  print('                  '+rooms[r165]['mmc']+'---------                                          ')
  print('                    |         '+rooms[r160]['mmc']+'--------------                         ')
  print('       '+rooms[r166]['mmc']+'--------     '+connect[179]['display']+'|        '+rooms[r160]['mmc']+'|              |                        ')
  print('      '+rooms[r166]['mmc']+'|        |    '+connect[179]['display']+'|   '+rooms[r161]['mmc']+'[ ]'+connect[175]['display']+'--'+rooms[r160]['mmc']+'|              |      '+rooms[r159]['mmc']+'--------          ')
  print('      '+rooms[r166]['mmc']+'|        |'+connect[180]['display']+'---'+rooms[r164]['mmc']+'[ ]       '+rooms[r160]['mmc']+'|              |'+connect[174]['display']+'-----'+rooms[r159]['mmc']+'|        |         ')
  print('       '+rooms[r166]['mmc']+'--------     '+connect[178]['display']+'|         '+rooms[r160]['mmc']+'--------------      '+rooms[r159]['mmc']+'|        |         ')
  print('        '+connect[181]['display']+'|          '+rooms[r163]['mmc']+'----        '+connect[176]['display']+'|                  '+rooms[r159]['mmc']+'|        |         ')
  print('       '+rooms[r167]['mmc']+'[ ]        '+rooms[r163]['mmc']+'|    |'+connect[177]['display']+'------'+rooms[r162]['mmc']+'[ ]                  '+rooms[r159]['mmc']+'--------          ')
  print('        '+connect[182]['display']+'|          '+rooms[r163]['mmc']+'----                               '+connect[173]['display']+'|              ')
  print('      '+rooms[r168]['mmc']+'-----                                          '+rooms[r158]['mmc']+'---             ')
  print(' '+rooms[r168]['mmc']+'....|     |                                        '+rooms[r158]['mmc']+'|   |            ')
  print('      '+rooms[r168]['mmc']+'-----                                         '+rooms[r158]['mmc']+'|   |            ')
  print('                                                    '+rooms[r158]['mmc']+'|   |            ')
  print('                                                     '+rooms[r158]['mmc']+'---             ')
  print('                                                      '+connect[172]['display']+':              ')
  print('                                                      '+connect[172]['display']+':              ')




room0C = Fore.RESET

rooms = {r0:{'type':r0   ,'left':'blank' ,'right':'blank' ,'up':r1      ,'down':'blank' ,'item':'blank'                ,'inspect':r0d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':True},
         r1:{'type':r1   ,'left':r2      ,'right':r3      ,'up':'blank' ,'down':r0      ,'item':'blank'                ,'inspect':r1d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r2:{'type':r2   ,'left':r4      ,'right':r1      ,'up':r5      ,'down':'blank' ,'item':'Food (Small)'         ,'inspect':r2d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r3:{'type':r3   ,'left':r1      ,'right':'blank' ,'up':r8      ,'down':'blank' ,'item':'blank'                ,'inspect':r3d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r4:{'type':r4   ,'left':'blank' ,'right':r2      ,'up':r10     ,'down':'blank' ,'item':'Map (Crypts)'         ,'inspect':r4d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r5:{'type':r5   ,'left':r10     ,'right':r6      ,'up':r16     ,'down':r2      ,'item':'Food (Small)'         ,'inspect':r5d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': r5BM, 'seen':False},
         r6:{'type':r6   ,'left':r5      ,'right':r7      ,'up':'blank' ,'down':r9      ,'item':'blank'                ,'inspect':r6d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r7:{'type':r7   ,'left':r6      ,'right':'blank' ,'up':'blank' ,'down':r8      ,'item':'Food (Small)'         ,'inspect':r7d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r8:{'type':r8   ,'left':'blank' ,'right':'blank' ,'up':r7      ,'down':r3      ,'item':'Lantern'              ,'inspect':r8d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r9:{'type':r9   ,'left':'blank' ,'right':'blank' ,'up':r6      ,'down':'blank' ,'item':'Crown'                ,'inspect':r9d, 'map':'f1' , 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r10:{'type':r10 ,'left':r11     ,'right':r5      ,'up':r14     ,'down':r4      ,'item':'blank'                ,'inspect':r10d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r11:{'type':r11 ,'left':'blank' ,'right':r10     ,'up':r12     ,'down':'blank ','item':'Rusty Sword'          ,'inspect':r11d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r12:{'type':r12 ,'left':'blank' ,'right':'blank' ,'up':r13     ,'down':r11     ,'item':'Explosive Charge'     ,'inspect':r12d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'large'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r13:{'type':r13 ,'left':'blank' ,'right':r14     ,'up':'blank' ,'down':r12     ,'item':'KEY TO CRIMSON CAVES' ,'inspect':r13d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'medium' ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r14:{'type':r14 ,'left':r13     ,'right':r15     ,'up':'blank' ,'down':r10     ,'item':'blank'                ,'inspect':r14d, 'map':'f1', 'minimap':'ice'      ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r15:{'type':r15 ,'left':r14     ,'right':'blank' ,'up':'blank' ,'down':r16     ,'item':'blank'                ,'inspect':r15d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r16:{'type':r16 ,'left':'blank' ,'right':r17     ,'up':r15     ,'down':r5      ,'item':'blank'                ,'inspect':r16d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r17:{'type':r17 ,'left':r16     ,'right':r19     ,'up':r18     ,'down':'blank','item':'blank'                ,'inspect':r17d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r18:{'type':r18 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r17     ,'item':'Lava Splash (Scroll)' ,'inspect':r18d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r19:{'type':r19 ,'left':r17     ,'right':'blank' ,'up':r20     ,'down':r21     ,'item':'blank'                ,'inspect':r19d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r20:{'type':r20 ,'left':'blank' ,'right':r24     ,'up':'blank' ,'down':r19     ,'item':'blank'                ,'inspect':r20d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r21:{'type':r21 ,'left':'blank' ,'right':r23     ,'up':r19     ,'down':'blank','item':'blank'                ,'inspect':r21d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r22:{'type':r22 ,'left':'blank' ,'right':'blank' ,'up':r23     ,'down':'blank','item':'Leather Armour'       ,'inspect':r22d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r23:{'type':r23 ,'left':r21     ,'right':'blank' ,'up':r24     ,'down':r22     ,'item':'blank'                ,'inspect':r23d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r24:{'type':r24 ,'left':'blank' ,'right':r25     ,'up':r20     ,'down':r23     ,'item':'blank'                ,'inspect':r24d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r24BM, 'seen':False},
         r25:{'type':r25 ,'left':r24     ,'right':'blank' ,'up':'blank' ,'down':'blank','item':'blank'                ,'inspect':r25d, 'map':'f1', 'minimap':'crypt'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r26:{'type':r26 ,'left':'blank' ,'right':'blank' ,'up':r27     ,'down':r25     ,'item':'blank'                ,'inspect':r26d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r27:{'type':r27 ,'left':r28     ,'right':r35     ,'up':'blank' ,'down':r26     ,'item':'blank'                ,'inspect':r27d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r28:{'type':r28 ,'left':r29     ,'right':r27     ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r28d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r29:{'type':r29 ,'left':'blank' ,'right':r28     ,'up':r30     ,'down':'blank' ,'item':'Pickaxe'              ,'inspect':r29d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r29BM, 'seen':False},
         r30:{'type':r30 ,'left':'blank' ,'right':r31     ,'up':'blank' ,'down':r29     ,'item':'Food (Medium)'        ,'inspect':r30d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r31:{'type':r31 ,'left':r30     ,'right':r32     ,'up':r43     ,'down':r40     ,'item':'blank'                ,'inspect':r31d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r32:{'type':r32 ,'left':r31     ,'right':r33     ,'up':'blank' ,'down':'blank' ,'item':'Map (Crimson Caves)'  ,'inspect':r32d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'safe','rest':'y' , 'bmap': Nbm, 'seen':False},
         r33:{'type':r33 ,'left':r32     ,'right':r34     ,'up':r41     ,'down':'blank' ,'item':'blank'                ,'inspect':r33d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r34:{'type':r34 ,'left':r33     ,'right':'blank' ,'up':'blank' ,'down':r35     ,'item':'blank'                ,'inspect':r34d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r35:{'type':r35 ,'left':r27     ,'right':r36     ,'up':r34     ,'down':'blank' ,'item':'blank'                ,'inspect':r35d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r35BM, 'seen':False},
         r36:{'type':r36 ,'left':r35     ,'right':'blank' ,'up':r38     ,'down':r37     ,'item':'Food (Medium)'        ,'inspect':r36d, 'map':'f2','minimap': 'wastes'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r37:{'type':r37 ,'left':'blank' ,'right':'blank' ,'up':r36     ,'down':'blank' ,'item':'Fire Bolt (Scroll)'   ,'inspect':r37d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r38:{'type':r38 ,'left':'blank' ,'right':'blank' ,'up':r39     ,'down':r36     ,'item':'blank'                ,'inspect':r38d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r39:{'type':r39 ,'left':r41     ,'right':'blank' ,'up':'blank' ,'down':r38     ,'item':'Food (Small)'         ,'inspect':r39d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r40:{'type':r40 ,'left':'blank' ,'right':'blank' ,'up':r31     ,'down':'blank' ,'item':'Mining Gear'          ,'inspect':r40d, 'map':'f2','minimap':'wastes'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r41:{'type':r41 ,'left':r42     ,'right':r39     ,'up':r45     ,'down':r33     ,'item':'Crown'                ,'inspect':r41d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r42:{'type':r42 ,'left':r43     ,'right':r41     ,'up':r44     ,'down':'blank' ,'item':'blank'                ,'inspect':r42d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r43:{'type':r43 ,'left':'blank' ,'right':r42     ,'up':'blank' ,'down':r31     ,'item':'Scorched Chainmail'   ,'inspect':r43d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r44:{'type':r44 ,'left':'blank' ,'right':'blank' ,'up':r46     ,'down':r42     ,'item':'blank'                ,'inspect':r44d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r45:{'type':r45 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r41     ,'item':'Crown'                ,'inspect':r45d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r46:{'type':r46 ,'left':r56     ,'right':r47     ,'up':'blank' ,'down':r44     ,'item':'blank'                ,'inspect':r46d, 'map':'f2','minimap':'deltas'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r46BM, 'seen':False},
         r47:{'type':r47 ,'left':r46     ,'right':r50     ,'up':r55     ,'down':r48     ,'item':'blank'                ,'inspect':r47d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r48:{'type':r48 ,'left':'blank' ,'right':'blank' ,'up':r47     ,'down':'blank' ,'item':'Steel Sword'          ,'inspect':r48d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r49:{'type':r49 ,'left':'blank' ,'right':r51     ,'up':r50     ,'down':'blank' ,'item':'blank'                ,'inspect':r49d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r50:{'type':r50 ,'left':r47     ,'right':'blank' ,'up':'blank' ,'down':r49     ,'item':'blank'                ,'inspect':r50d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r50BM, 'seen':False},
         r51:{'type':r51 ,'left':r49     ,'right':'blank' ,'up':r52     ,'down':'blank' ,'item':'Tesla Coil (Scroll)'  ,'inspect':r51d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r52:{'type':r52 ,'left':r53     ,'right':'blank' ,'up':'blank' ,'down':r51     ,'item':'blank'                ,'inspect':r52d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r52BM, 'seen':False},
         r53:{'type':r53 ,'left':'blank' ,'right':r52     ,'up':r54     ,'down':'blank' ,'item':'blank'                ,'inspect':r53d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r54:{'type':r54 ,'left':'blank' ,'right':'blank' ,'up':r76     ,'down':r53     ,'item':'blank'                ,'inspect':r54d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r55:{'type':r55 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r47     ,'item':'Heal Potion (Small)'  ,'inspect':r55d, 'map':'f2','minimap':'lockhouse' ,'mmc': Fore.RESET ,'size':'large','rest':'n', 'bmap': r55BM, 'seen':False},
         r56:{'type':r56 ,'left':r61     ,'right':r46     ,'up':r59     ,'down':r57     ,'item':'blank'                ,'inspect':r56d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r57:{'type':r57 ,'left':'blank' ,'right':'blank' ,'up':r56     ,'down':r58     ,'item':'blank'                ,'inspect':r57d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r57BM, 'seen':False},
         r58:{'type':r58 ,'left':'blank' ,'right':'blank' ,'up':r57     ,'down':'blank' ,'item':'Guard Chainmail'      ,'inspect':r58d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r59:{'type':r59 ,'left':r60     ,'right':'blank' ,'up':'blank' ,'down':r56     ,'item':'Acid Bullet (Scroll)' ,'inspect':r59d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r59BM, 'seen':False},
         r60:{'type':r60 ,'left':'blank' ,'right':r59     ,'up':r62     ,'down':r61     ,'item':'blank'                ,'inspect':r60d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r60BM, 'seen':False},
         r61:{'type':r61 ,'left':'blank' ,'right':r56     ,'up':r60     ,'down':'blank' ,'item':'Web (Scroll)'         ,'inspect':r61d, 'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r62:{'type':r62 ,'left':'blank' ,'right':'blank' ,'up':r63     ,'down':r60     ,'item':'blank'                ,'inspect':r62d ,'map':'f2','minimap':'spiders'   ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r63:{'type':r63 ,'left':'blank' ,'right':r64     ,'up':'blank' ,'down':r62     ,'item':'blank'                ,'inspect':r63d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r64:{'type':r64 ,'left':r63     ,'right':r65     ,'up':r66     ,'down':'blank' ,'item':'blank'                ,'inspect':r64d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r65:{'type':r65 ,'left':r64     ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Spores (Scroll)'      ,'inspect':r65d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r66:{'type':r66 ,'left':'blank' ,'right':r67     ,'up':r69     ,'down':r64     ,'item':'Food (Large)'         ,'inspect':r66d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r66BM, 'seen':False},
         r67:{'type':r67 ,'left':r66     ,'right':r68     ,'up':r72     ,'down':'blank' ,'item':'blank'                ,'inspect':r67d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r68:{'type':r68 ,'left':r67     ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Heal Potion (Medium)' ,'inspect':r68d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r68BM, 'seen':False},
         r69:{'type':r69 ,'left':r71     ,'right':'blank' ,'up':r70     ,'down':r66     ,'item':'blank'                ,'inspect':r69d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r70:{'type':r70 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r69     ,'item':'Shroomal Sythe'       ,'inspect':r70d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r71:{'type':r71 ,'left':'blank' ,'right':r69     ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r71d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r71BM, 'seen':False},
         r72:{'type':r72 ,'left':'blank' ,'right':r73     ,'up':'blank' ,'down':r67     ,'item':'blank'                ,'inspect':r72d ,'map':'f21','minimap':'shrooms'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r73:{'type':r73 ,'left':r72     ,'right':r74     ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r73d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r74:{'type':r74 ,'left':r73     ,'right':'blank' ,'up':r75     ,'down':'blank' ,'item':'blank'                ,'inspect':r74d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r75:{'type':r75 ,'left':r85     ,'right':r81     ,'up':r88     ,'down':r74     ,'item':'Map (Crossroads)'     ,'inspect':r75d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r75BM, 'seen':False},
         r76:{'type':r76 ,'left':'blank' ,'right':r78     ,'up':r77     ,'down':r54     ,'item':'blank'                ,'inspect':r76d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r77:{'type':r77 ,'left':'blank' ,'right':r80     ,'up':'blank' ,'down':r76     ,'item':'Food (Medium)'        ,'inspect':r77d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r78:{'type':r78 ,'left':r76     ,'right':r79     ,'up':r80     ,'down':'blank' ,'item':'blank'                ,'inspect':r78d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r78BM, 'seen':False},
         r79:{'type':r79 ,'left':r78     ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Half Plate'           ,'inspect':r79d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r80:{'type':r80 ,'left':r77     ,'right':'blank' ,'up':r81     ,'down':r78     ,'item':'blank'                ,'inspect':r80d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r80BM, 'seen':False},
         r81:{'type':r81 ,'left':r75     ,'right':'blank' ,'up':r82     ,'down':r80     ,'item':'blank'                ,'inspect':r81d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r82:{'type':r82 ,'left':'blank' ,'right':r83     ,'up':'blank' ,'down':r81     ,'item':'blank'                ,'inspect':r82d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r83:{'type':r83 ,'left':r82     ,'right':'blank' ,'up':'blank' ,'down':r84     ,'item':'blank'                ,'inspect':r83d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r84:{'type':r84 ,'left':'blank' ,'right':'blank' ,'up':r83     ,'down':'blank' ,'item':'Lightning Dagger'     ,'inspect':r84d ,'map':'f21','minimap':'caves'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r84BM, 'seen':False},
         r85:{'type':r85 ,'left':'blank' ,'right':r75     ,'up':r86     ,'down':'blank' ,'item':'blank'                ,'inspect':r85d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r86:{'type':r86 ,'left':r90     ,'right':r87     ,'up':r94     ,'down':r85     ,'item':'Heal Potion (Small)'  ,'inspect':r86d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r86BM, 'seen':False},
         r87:{'type':r87 ,'left':r86     ,'right':r88     ,'up':r89     ,'down':'blank' ,'item':'blank'                ,'inspect':r87d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r88:{'type':r88 ,'left':r87     ,'right':'blank' ,'up':'blank' ,'down':r75     ,'item':'blank'                ,'inspect':r88d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r89:{'type':r89 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r87     ,'item':'Vine Wrap (Scroll)'   ,'inspect':r89d ,'map':'f21','minimap':'mists'    ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r90:{'type':r90 ,'left':'blank' ,'right':r86     ,'up':'blank' ,'down':r91     ,'item':'Fireball (Scroll)'    ,'inspect':r90d ,'map':'f21','minimap':'parlour'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r91:{'type':r91 ,'left':'blank' ,'right':'blank' ,'up':r90     ,'down':r92     ,'item':'blank'                ,'inspect':r91d ,'map':'f21','minimap':'parlour'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r91BM, 'seen':False},
         r92:{'type':r92 ,'left':r93     ,'right':'blank' ,'up':r91     ,'down':'blank' ,'item':'blank'                ,'inspect':r92d ,'map':'f21','minimap':'parlour'  ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r93:{'type':r93 ,'left':'blank' ,'right':r92     ,'up':'blank' ,'down':'blank' ,'item':'Staff of the Magi'    ,'inspect':r93d ,'map':'f21','minimap':'parlour'  ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r94:{'type':r94 ,'left':'blank' ,'right':r96     ,'up':r95     ,'down':r86     ,'item':'blank'                ,'inspect':r94d ,'map':'f21','minimap':'river'    ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r95:{'type':r95 ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r94     ,'item':'Grand Crown'          ,'inspect':r95d ,'map':'f21','minimap':'river'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r96:{'type':r96 ,'left':r94     ,'right':r97     ,'up':'blank' ,'down':'blank' ,'item':'Crown'                ,'inspect':r96d ,'map':'f21','minimap':'river'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r97:{'type':r97 ,'left':r96     ,'right':'blank' ,'up':'blank' ,'down':r98     ,'item':'Waterfall (Scroll)'   ,'inspect':r97d ,'map':'f21','minimap':'river'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r98:{'type':r98 ,'left':r99     ,'right':'blank' ,'up':r97     ,'down':'blank' ,'item':'blank'                ,'inspect':r98d ,'map':'f21','minimap':'river'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r99:{'type':r99 ,'left':'blank' ,'right':r98     ,'up':'blank' ,'down':r100    ,'item':'Food (Medium)'        ,'inspect':r99d ,'map':'f21','minimap':'river'    ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r100:{'type':r100 ,'left':'blank' ,'right':r100tr ,'up':r99    ,'down':'blank' ,'item':'blank'                ,'inspect':r100d ,'map':'f21','minimap':'river'   ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': r100BM, 'seen':False},
         r100tr:{'type':r100tr ,'left':r100 ,'right':r101 ,'up':'blank' ,'down':'blank' ,'item':'blank'                ,'inspect':r100trd ,'map':'f21','minimap':'river' ,'mmc': Fore.RESET,'size':'large','rest':'n', 'bmap': Nbm, 'seen':False},
         r101:{'type':r101   ,'left':'blank' ,'right':'blank' ,'up':r102    ,'down':r100tr  ,'item':'blank'            ,'inspect':r101d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r102:{'type':r102   ,'left':r103    ,'right':'blank' ,'up':r108    ,'down':r101    ,'item':'blank'            ,'inspect':r102d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r103:{'type':r103   ,'left':r104    ,'right':r102    ,'up':'blank' ,'down':'blank' ,'item':'Food (Large)'     ,'inspect':r103d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': r103BM, 'seen':False},
         r104:{'type':r104   ,'left':'blank' ,'right':r103    ,'up':r106    ,'down':r105    ,'item':'blank'            ,'inspect':r104d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r105:{'type':r105   ,'left':'blank' ,'right':'blank' ,'up':r104    ,'down':'blank' ,'item':'Ocean Reaver'     ,'inspect':r105d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r106:{'type':r106   ,'left':r107    ,'right':r108    ,'up':'blank' ,'down':r104    ,'item':'blank'            ,'inspect':r106d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r107:{'type':r107   ,'left':'blank' ,'right':r106    ,'up':'blank' ,'down':'blank' ,'item':'Boat'             ,'inspect':r107d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': r107BM, 'seen':False},
         r108:{'type':r108   ,'left':r106    ,'right':r109    ,'up':r110    ,'down':r102    ,'item':'blank'            ,'inspect':r108d, 'map':'f21' , 'minimap':'lakes' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r109:{'type':r109   ,'left':r108    ,'right':r126    ,'up':r120    ,'down':r123    ,'item':'blank'            ,'inspect':r109d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r110:{'type':r110   ,'left':r118    ,'right':r119    ,'up':r111    ,'down':r108    ,'item':'blank'            ,'inspect':r110d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r111:{'type':r111   ,'left':'blank' ,'right':'blank' ,'up':r112    ,'down':r110    ,'item':'blank'            ,'inspect':r111d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r112:{'type':r112   ,'left':r114    ,'right':r113    ,'up':r115    ,'down':r111    ,'item':'blank'            ,'inspect':r112d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r113:{'type':r113   ,'left':r112    ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Grand Crown'      ,'inspect':r113d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r114:{'type':r114   ,'left':'blank' ,'right':r112    ,'up':'blank' ,'down':'blank' ,'item':'Map (Lagoon)'     ,'inspect':r114d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': r114BM, 'seen':False},
         r115:{'type':r115   ,'left':r117    ,'right':'blank' ,'up':r116    ,'down':r112    ,'item':'blank'            ,'inspect':r115d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': r115BM, 'seen':False},
         r116:{'type':r116   ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r115    ,'item':'Heal Potion (Medium)','inspect':r116d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'safe','rest':'y', 'bmap': Nbm, 'seen':False},
         r117:{'type':r117   ,'left':'blank' ,'right':r115    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r117d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r118:{'type':r118   ,'left':'blank' ,'right':r110    ,'up':'blank' ,'down':'blank' ,'item':'Blunderbuss'      ,'inspect':r118d, 'map':'f21' , 'minimap':'ship'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r119:{'type':r119   ,'left':r110    ,'right':r121    ,'up':'blank' ,'down':r120    ,'item':'blank'            ,'inspect':r119d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r120:{'type':r120   ,'left':'blank' ,'right':'blank' ,'up':r119    ,'down':r109    ,'item':'blank'            ,'inspect':r120d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r121:{'type':r121   ,'left':r119    ,'right':'blank' ,'up':'blank' ,'down':r122    ,'item':'Cannonball'       ,'inspect':r121d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': r121BM, 'seen':False},
         r122:{'type':r122   ,'left':'blank' ,'right':'blank' ,'up':r121    ,'down':'blank' ,'item':'Smite (Scroll)'   ,'inspect':r122d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r123:{'type':r123   ,'left':'blank' ,'right':r124    ,'up':r109    ,'down':'blank' ,'item':'blank'            ,'inspect':r123d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r124:{'type':r124   ,'left':r123    ,'right':r125    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r124d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r125:{'type':r125   ,'left':r124    ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'Scale Mail'       ,'inspect':r125d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r126:{'type':r126   ,'left':r109    ,'right':r127    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r126d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': r126BM, 'seen':False},
         r127:{'type':r127   ,'left':r126    ,'right':r128    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r127d, 'map':'f21' , 'minimap':'hold'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r128:{'type':r128   ,'left':r127 ,'right':r133    ,'up':r129    ,'down':r127    ,'item':'blank'               ,'inspect':r128d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r129:{'type':r129   ,'left':'blank' ,'right':'blank' ,'up':r130    ,'down':r128    ,'item':'blank'            ,'inspect':r129d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r130:{'type':r130   ,'left':'blank' ,'right':r132    ,'up':r131    ,'down':r129    ,'item':'blank'            ,'inspect':r130d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r131:{'type':r131   ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r130    ,'item':'blank'            ,'inspect':r131d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r132:{'type':r132   ,'left':r130    ,'right':r135    ,'up':r144    ,'down':'blank' ,'item':'blank'            ,'inspect':r132d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r133:{'type':r133   ,'left':r128    ,'right':r134    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r133d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r134:{'type':r134   ,'left':r133    ,'right':'blank' ,'up':r135    ,'down':'blank' ,'item':'blank'            ,'inspect':r134d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r135:{'type':r135   ,'left':r132    ,'right':r136    ,'up':'blank' ,'down':r134    ,'item':'blank'            ,'inspect':r135d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r136:{'type':r136   ,'left':r135    ,'right':'blank' ,'up':r137    ,'down':'blank' ,'item':'blank'            ,'inspect':r136d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r137:{'type':r137   ,'left':r139    ,'right':r138    ,'up':'blank' ,'down':r136    ,'item':'blank'            ,'inspect':r137d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r138:{'type':r138   ,'left':r137    ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r138d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r139:{'type':r139   ,'left':'blank' ,'right':r137    ,'up':r140    ,'down':'blank' ,'item':'blank'            ,'inspect':r139d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r140:{'type':r140   ,'left':'blank' ,'right':r141    ,'up':'blank' ,'down':r139    ,'item':'blank'            ,'inspect':r140d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r141:{'type':r141   ,'left':r140    ,'right':'blank' ,'up':r142    ,'down':'blank' ,'item':'blank'            ,'inspect':r141d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r142:{'type':r142   ,'left':'blank' ,'right':r143    ,'up':'blank' ,'down':r141    ,'item':'blank'            ,'inspect':r142d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r143:{'type':r143   ,'left':r142    ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r143d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r144:{'type':r144   ,'left':r145    ,'right':'blank' ,'up':'blank' ,'down':r132    ,'item':'blank'            ,'inspect':r144d, 'map':'f21' , 'minimap':'haunt' ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r145:{'type':r145   ,'left':'blank' ,'right':r144    ,'up':r146    ,'down':'blank' ,'item':'blank'            ,'inspect':r145d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r146:{'type':r146   ,'left':'blank' ,'right':r147    ,'up':'blank' ,'down':r145    ,'item':'blank'            ,'inspect':r146d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r147:{'type':r147   ,'left':r146    ,'right':r149    ,'up':'blank' ,'down':r148    ,'item':'blank'            ,'inspect':r147d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r148:{'type':r148   ,'left':'blank' ,'right':'blank' ,'up':r147    ,'down':'blank' ,'item':'blank'            ,'inspect':r148d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r149:{'type':r149   ,'left':r147    ,'right':r150    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r149d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r150:{'type':r150   ,'left':r149    ,'right':'blank' ,'up':'blank' ,'down':r152    ,'item':'blank'            ,'inspect':r150d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r151:{'type':r151   ,'left':'blank' ,'right':r152    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r151d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r152:{'type':r152   ,'left':r151    ,'right':r154    ,'up':r150    ,'down':r153    ,'item':'blank'            ,'inspect':r152d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r153:{'type':r153   ,'left':'blank' ,'right':'blank' ,'up':r152    ,'down':'blank' ,'item':'blank'            ,'inspect':r153d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r154:{'type':r154   ,'left':r152    ,'right':'blank' ,'up':r158    ,'down':r155    ,'item':'blank'            ,'inspect':r154d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},       
         r155:{'type':r155   ,'left':r156    ,'right':r157    ,'up':r154    ,'down':'blank' ,'item':'blank'            ,'inspect':r155d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r156:{'type':r156   ,'left':'blank' ,'right':r155    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r156d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r157:{'type':r157   ,'left':r155    ,'right':'blank' ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r157d, 'map':'f21' , 'minimap':'wisp'  ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r158:{'type':r158   ,'left':'blank' ,'right':'blank' ,'up':r159    ,'down':r154    ,'item':'blank'            ,'inspect':r158d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r159:{'type':r159   ,'left':r160    ,'right':'blank' ,'up':'blank' ,'down':r158    ,'item':'blank'            ,'inspect':r159d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r160:{'type':r160   ,'left':r161    ,'right':r159    ,'up':'blank' ,'down':r162    ,'item':'blank'            ,'inspect':r160d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r161:{'type':r161   ,'left':'blank' ,'right':r160    ,'up':'blank' ,'down':'blank' ,'item':'blank'            ,'inspect':r161d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r162:{'type':r162   ,'left':r163    ,'right':r160    ,'up':r160    ,'down':'blank' ,'item':'blank'            ,'inspect':r162d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r163:{'type':r163   ,'left':'blank' ,'right':r162    ,'up':r164    ,'down':'blank' ,'item':'blank'            ,'inspect':r163d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r164:{'type':r164   ,'left':r166    ,'right':'blank' ,'up':r165    ,'down':r163    ,'item':'blank'            ,'inspect':r164d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r165:{'type':r165   ,'left':'blank' ,'right':'blank' ,'up':'blank' ,'down':r164    ,'item':'blank'            ,'inspect':r165d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r166:{'type':r166   ,'left':'blank' ,'right':r164    ,'up':'blank' ,'down':r167    ,'item':'blank'            ,'inspect':r166d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False},
         r167:{'type':r167   ,'left':'blank' ,'right':'blank' ,'up':r166    ,'down':r168    ,'item':'blank'            ,'inspect':r167d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'safe'   ,'rest':'y', 'bmap': Nbm, 'seen':False},
         r168:{'type':r168   ,'left':'blank' ,'right':'blank' ,'up':r167    ,'down':'blank' ,'item':'blank'            ,'inspect':r168d, 'map':'f21' , 'minimap':'dark'  ,'mmc': Fore.RESET,'size':'small'  ,'rest':'n', 'bmap': Nbm, 'seen':False}}








for n in rooms:
  rooms[n]['seen'] = 0
rooms[r0]['seen'] = 1


spList = ['Freeze Mist (Scroll)']
class P:
  def __init__(self,CRoom,H,weapon,armour,PreRoom,CTile,SP,x,y,speed,xp,level,maxH,spellSL,spellList,normSP,lastRest):
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
    self.normSP = normSP
    self.lastRest = lastRest
Player = P(r0,100,'Wood Staff','Travel Cloak',r0,250,3,1,1,3,0,1,100,3,spList,3,r0)






items = {'Wood Staff':{'equ':'wea','heal':'n','type':'blunt','pow':10,'def':'n','num':1,'wEquiped':'yes','aEquiped':'no','conditions':'n','weight': 0, 'index': 1, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Freeze Mist (Scroll)':{'equ':'spe','heal':'n','type':'cold','pow':30,'def':'n','num':1,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'yes', 'aoe': '', 'rad': ''},
'Travel Cloak':{'equ':'arm','heal':'n','type':'n','pow':'n','def':10,'num':1,'wEquiped':'no','aEquiped':'yes','conditions':'n','weight': 0, 'index': 2, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Food (Small)':{'equ':'n','heal':20,'type':'n','pow':'n','def':'n','num':3,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Lantern':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Crown':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Lava Splash (Scroll)':{'equ':'spe','heal':'n','type':'fire','pow':30,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y', 'rad': 1},
'Rusty Sword':{'equ':'wea','heal':'n','type':'slash','pow':30,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'index': 3, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Explosive Charge':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Leather Armour':{'equ':'arm','heal':'n','type':'n','pow':'n','def':20,'num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 0, 'index': 4, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'KEY TO CRIMSON CAVES':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num': 0,'wEquiped':'no','aEquiped':'no','conditions':'y','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Map (Crypts)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Pickaxe':{'equ':'wea','heal':'n','type':'slash','pow':40,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 2, 'index': 5, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Food (Medium)':{'equ':'n','heal':50,'type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Map (Crimson Caves)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Fire Bolt (Scroll)':{'equ':'spe','heal':'n','type':'fire','pow':55,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Mining Gear':{'equ':'arm','heal':'n','type':'n','pow':'n','def':25,'num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 1, 'index': 6, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Scorched Chainmail':{'equ':'arm','heal':'n','type':'n','pow':'n','def':35,'num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 3, 'index': 7, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Steel Sword':{'equ':'wea','heal':'n','type':'slash','pow':50,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 1, 'index': 8, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Tesla Coil (Scroll)':{'equ':'spe','heal':'n','type':'shock','pow':65,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Heal Potion (Small)':{'equ':'n','heal':40,'type':'n','pow':'n','def':'','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Guard Chainmail':{'equ':'arm','heal':'n','type':'n','pow':'n','def':40,'num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': 3, 'index': 9, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Acid Bullet (Scroll)':{'equ':'spe','heal':'n','type':'acid','pow':65,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Web (Scroll)':{'equ':'spe','heal':'n','type':'acid','pow':10,'def':'n','num':0,'wEquiped':'no','aEquiped':' no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y', 'rad': 1},
'Spores (Scroll)':{'equ':'spe','heal':'n','type':'acid','pow':45,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y', 'rad': 3},
'Shroomal Sythe':{'equ':'wea','heal':'n','type':'acid','pow':55,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'index': 10, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Food (Large)':{'equ':'n','heal':80,'type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Heal Potion (Medium)':{'equ':'n','heal':60,'type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Map (Crossroads)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Half Plate':{'equ':'arm','heal':'n','type':'n','pow':'n','def':50,'num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 3, 'index': 11, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Lightning Dagger':{'equ':'wea','heal':'n','type':'shock','pow':30,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': -2, 'index': 12, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Vine Wrap (Scroll)':{'equ':'spe','heal':'n','type':'nature','pow':55,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Fireball (Scroll)':{'equ':'spe','heal':'n','type':'fire','pow':60,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y', 'rad': 2},
'Staff of the Magi':{'equ':'wea','heal':'n','type':'blunt','pow':50,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'index': 13, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Grand Crown':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Waterfall (Scroll)':{'equ':'spe','heal':'n','type':'water','pow':80,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Ocean Reaver':{'equ':'wea','heal':'n','type':'water','pow':60,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 2, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Boat':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Map (Lagoon)':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Blunderbuss':{'equ':'wea','heal':'n','type':'pierce','pow':45,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Cannonball':{'equ':'n','heal':'n','type':'n','pow':'n','def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': '', 'rad': ''},
'Smite (Scroll)':{'equ':'spe','heal':'n','type':'radiant','pow':40,'def':'n','num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': '', 'sEquiped': 'no', 'aoe': 'y', 'rad': 1},
'Scale Mail':{'equ':'arm','heal':'n','type':'n','pow':'n','def':40,'num':0,'wEquiped':'no','aEquiped':'no','conditions':'n','weight': 1, 'sEquiped': 'no', 'aoe': '', 'rad': ''}}










connect = {
  1:{'c1':r0, 'c2':r1, 'display':Fore.RESET},
  2:{'c1':r1, 'c2':r2, 'display':fg(0)},
  3:{'c1':r2, 'c2':r4, 'display':fg(0)},
  4:{'c1':r1, 'c2':r3, 'display':fg(0)},
  5:{'c1':r2, 'c2':r5, 'display':fg(0)},
  6:{'c1':r3, 'c2':r8, 'display':fg(0)},
  7:{'c1':r4, 'c2':r10, 'display':fg(0)},
  8:{'c1':r8, 'c2':r7, 'display':fg(0)},
  9:{'c1':r7, 'c2':r6, 'display':fg(0)},
  10:{'c1':r6, 'c2':r9, 'display':fg(0)},
  11:{'c1':r5, 'c2':r6, 'display':fg(0)},
  12:{'c1':r5, 'c2':r10, 'display':fg(0)},
  13:{'c1':r10, 'c2':r11, 'display':fg(0)},
  14:{'c1':r11, 'c2':r12, 'display':fg(0)},
  15:{'c1':r12, 'c2':r13, 'display':fg(0)},
  16:{'c1':r13, 'c2':r14, 'display':fg(0)},
  17:{'c1':r10, 'c2':r14, 'display':fg(0)},
  18:{'c1':r14, 'c2':r15, 'display':fg(0)},
  19:{'c1':r5, 'c2':r16, 'display':fg(0)},
  20:{'c1':r15, 'c2':r16, 'display':fg(0)},
  21:{'c1':r16, 'c2':r17, 'display':fg(0)},
  22:{'c1':r17, 'c2':r18, 'display':fg(0)},
  23:{'c1':r17, 'c2':r19, 'display':fg(0)},
  24:{'c1':r19, 'c2':r21, 'display':fg(0)},
  25:{'c1':r21, 'c2':r23, 'display':fg(0)},
  26:{'c1':r23, 'c2':r22, 'display':fg(0)},
  27:{'c1':r23, 'c2':r24, 'display':fg(0)},
  28:{'c1':r19, 'c2':r20, 'display':fg(0)},
  29:{'c1':r20, 'c2':r24, 'display':fg(0)},
  30:{'c1':r24, 'c2':r25, 'display':fg(0)},
  31:{'c1':r25, 'c2':r26, 'display':fg(0)},
  32:{'c1':r26, 'c2':r27, 'display':fg(0)},
  33:{'c1':r27, 'c2':r28, 'display':fg(0)},
  34:{'c1':r28, 'c2':r29, 'display':fg(0)},
  35:{'c1':r29, 'c2':r30, 'display':fg(0)},
  36:{'c1':r30, 'c2':r31, 'display':fg(0)},
  37:{'c1':r31, 'c2':r32, 'display':fg(0)},
  38:{'c1':r32, 'c2':r33, 'display':fg(0)},
  39:{'c1':r33, 'c2':r34, 'display':fg(0)},
  40:{'c1':r34, 'c2':r35, 'display':fg(0)},
  41:{'c1':r27, 'c2':r35, 'display':fg(0)},
  42:{'c1':r35, 'c2':r36, 'display':fg(0)},
  43:{'c1':r36, 'c2':r37, 'display':fg(0)},
  44:{'c1':r36, 'c2':r38, 'display':fg(0)},
  45:{'c1':r38, 'c2':r39, 'display':fg(0)},
  46:{'c1':r39, 'c2':r41, 'display':fg(0)},
  47:{'c1':r33, 'c2':r41, 'display':fg(0)},
  48:{'c1':r41, 'c2':r45, 'display':fg(0)},
  49:{'c1':r41, 'c2':r42, 'display':fg(0)},
  50:{'c1':r42, 'c2':r43, 'display':fg(0)},
  51:{'c1':r31, 'c2':r43, 'display':fg(0)},
  52:{'c1':r42, 'c2':r44, 'display':fg(0)},
  53:{'c1':r44, 'c2':r46, 'display':fg(0)},
  54:{'c1':r46, 'c2':r47, 'display':fg(0)},
  55:{'c1':r47, 'c2':r55, 'display':fg(0)},
  56:{'c1':r47, 'c2':r48, 'display':fg(0)},
  57:{'c1':r47, 'c2':r50, 'display':fg(0)},
  58:{'c1':r50, 'c2':r49, 'display':fg(0)},
  59:{'c1':r49, 'c2':r51, 'display':fg(0)},
  60:{'c1':r51, 'c2':r52, 'display':fg(0)},
  61:{'c1':r52, 'c2':r53, 'display':fg(0)},
  62:{'c1':r53, 'c2':r54, 'display':fg(0)},
  63:{'c1':r46, 'c2':r56, 'display':fg(0)},
  64:{'c1':r56, 'c2':r57, 'display':fg(0)},
  65:{'c1':r57, 'c2':r58, 'display':fg(0)},
  66:{'c1':r56, 'c2':r61, 'display':fg(0)},
  67:{'c1':r61, 'c2':r60, 'display':fg(0)},
  68:{'c1':r56, 'c2':r59, 'display':fg(0)},
  69:{'c1':r59, 'c2':r60, 'display':fg(0)},
  70:{'c1':r60, 'c2':r61, 'display':fg(0)},
  71:{'c1':r62, 'c2':r63, 'display':fg(0)},
  72:{'c1':r63, 'c2':r64, 'display':fg(0)},
  73:{'c1':r64, 'c2':r65, 'display':fg(0)},
  74:{'c1':r64, 'c2':r66, 'display':fg(0)},
  75:{'c1':r66, 'c2':r69, 'display':fg(0)},
  76:{'c1':r69, 'c2':r70, 'display':fg(0)},
  77:{'c1':r69, 'c2':r71, 'display':fg(0)},
  78:{'c1':r66, 'c2':r67, 'display':fg(0)},
  79:{'c1':r67, 'c2':r72, 'display':fg(0)},
  80:{'c1':r67, 'c2':r68, 'display':fg(0)},
  81:{'c1':r72, 'c2':r73, 'display':fg(0)},
  82:{'c1':r73, 'c2':r74, 'display':fg(0)},
  83:{'c1':r74, 'c2':r75, 'display':fg(0)},
  84:{'c1':r54, 'c2':r76, 'display':fg(0)},
  85:{'c1':r76, 'c2':r77, 'display':fg(0)},
  86:{'c1':r77, 'c2':r80, 'display':fg(0)},
  87:{'c1':r76, 'c2':r78, 'display':fg(0)},
  88:{'c1':r78, 'c2':r79, 'display':fg(0)},
  89:{'c1':r78, 'c2':r80, 'display':fg(0)},
  90:{'c1':r80, 'c2':r81, 'display':fg(0)},
  91:{'c1':r81, 'c2':r82, 'display':fg(0)},
  92:{'c1':r82, 'c2':r83, 'display':fg(0)},
  93:{'c1':r83, 'c2':r84, 'display':fg(0)},
  94:{'c1':r81, 'c2':r75, 'display':fg(0)},
  95:{'c1':r75, 'c2':r85, 'display':fg(0)},
  96:{'c1':r85, 'c2':r86, 'display':fg(0)},
  97:{'c1':r75, 'c2':r88, 'display':fg(0)},
  98:{'c1':r88, 'c2':r87, 'display':fg(0)},
  99:{'c1':r87, 'c2':r89, 'display':fg(0)},
  100:{'c1':r87, 'c2':r86, 'display':fg(0)},
  101:{'c1':r86, 'c2':r90, 'display':fg(0)},
  102:{'c1':r90, 'c2':r91, 'display':fg(0)},
  103:{'c1':r91, 'c2':r92, 'display':fg(0)},
  104:{'c1':r92, 'c2':r93, 'display':fg(0)},
  105:{'c1':r86, 'c2':r94, 'display':fg(0)},
  106:{'c1':r94, 'c2':r95, 'display':fg(0)},
  107:{'c1':r94, 'c2':r96, 'display':fg(0)},
  108:{'c1':r96, 'c2':r97, 'display':fg(0)},
  109:{'c1':r97, 'c2':r98, 'display':fg(0)},
  110:{'c1':r98, 'c2':r99, 'display':fg(0)},
  111:{'c1':r99, 'c2':r100, 'display':fg(0)},
  112:{'c1':r100, 'c2':r100tr, 'display':fg(0)},
  113:{'c1':r100tr, 'c2':r101, 'display':fg(0)},
  114:{'c1':r101, 'c2':r102, 'display':fg(0)},
  115:{'c1':r102, 'c2':r108, 'display':fg(0)},
  116:{'c1':r102, 'c2':r103, 'display':fg(0)},
  117:{'c1':r103, 'c2':r104, 'display':fg(0)},
  118:{'c1':r104, 'c2':r106, 'display':fg(0)},
  119:{'c1':r104, 'c2':r105, 'display':fg(0)},
  120:{'c1':r106, 'c2':r107, 'display':fg(0)},
  121:{'c1':r106, 'c2':r108, 'display':fg(0)},
  122:{'c1':r108, 'c2':r111, 'display':fg(0)},
  141:{'c1':r110, 'c2':r111, 'display':fg(0)},
  123:{'c1':r111, 'c2':r112, 'display':fg(0)},
  124:{'c1':r112, 'c2':r115, 'display':fg(0)},
  125:{'c1':r112, 'c2':r113, 'display':fg(0)},
  126:{'c1':r112, 'c2':r114, 'display':fg(0)},
  127:{'c1':r115, 'c2':r116, 'display':fg(0)},
  128:{'c1':r115, 'c2':r117, 'display':fg(0)},
  129:{'c1':r110, 'c2':r118, 'display':fg(0)},
  130:{'c1':r110, 'c2':r119, 'display':fg(0)},
  131:{'c1':r119, 'c2':r120, 'display':fg(0)},
  132:{'c1':r120, 'c2':r109, 'display':fg(0)},
  133:{'c1':r119, 'c2':r121, 'display':fg(0)},
  134:{'c1':r121, 'c2':r122, 'display':fg(0)},
  135:{'c1':r108, 'c2':r109, 'display':fg(0)},
  136:{'c1':r109, 'c2':r123, 'display':fg(0)},
  137:{'c1':r123, 'c2':r124, 'display':fg(0)},
  138:{'c1':r124, 'c2':r125, 'display':fg(0)},
  139:{'c1':r109, 'c2':r126, 'display':fg(0)},
  140:{'c1':r126, 'c2':r127, 'display':fg(0)},
  141:{'c1':r127, 'c2':r128, 'display':fg(0)},
  142:{'c1':r128, 'c2':r129, 'display':fg(0)},
  143:{'c1':r129, 'c2':r130, 'display':fg(0)},
  144:{'c1':r130, 'c2':r131, 'display':fg(0)},
  145:{'c1':r130, 'c2':r132, 'display':fg(0)},
  146:{'c1':r128, 'c2':r133, 'display':fg(0)},
  147:{'c1':r133, 'c2':r134, 'display':fg(0)},
  148:{'c1':r134, 'c2':r135, 'display':fg(0)},
  149:{'c1':r135, 'c2':r132, 'display':fg(0)},
  150:{'c1':r135, 'c2':r136, 'display':fg(0)},
  151:{'c1':r136, 'c2':r137, 'display':fg(0)},
  152:{'c1':r137, 'c2':r138, 'display':fg(0)},
  153:{'c1':r137, 'c2':r139, 'display':fg(0)},
  154:{'c1':r139, 'c2':r140, 'display':fg(0)},
  155:{'c1':r140, 'c2':r141, 'display':fg(0)},
  156:{'c1':r141, 'c2':r142, 'display':fg(0)},
  157:{'c1':r142, 'c2':r143, 'display':fg(0)},
  158:{'c1':r132, 'c2':r144, 'display':fg(0)},
  159:{'c1':r144, 'c2':r145, 'display':fg(0)},
  160:{'c1':r145, 'c2':r146, 'display':fg(0)},
  161:{'c1':r146, 'c2':r147, 'display':fg(0)},
  162:{'c1':r147, 'c2':r148, 'display':fg(0)},
  163:{'c1':r147, 'c2':r149, 'display':fg(0)},
  164:{'c1':r149, 'c2':r150, 'display':fg(0)},
  165:{'c1':r150, 'c2':r152, 'display':fg(0)},
  166:{'c1':r152, 'c2':r151, 'display':fg(0)},
  167:{'c1':r152, 'c2':r153, 'display':fg(0)},
  168:{'c1':r152, 'c2':r154, 'display':fg(0)},
  169:{'c1':r154, 'c2':r155, 'display':fg(0)},
  170:{'c1':r155, 'c2':r156, 'display':fg(0)},
  171:{'c1':r155, 'c2':r157, 'display':fg(0)},
  172:{'c1':r154, 'c2':r158, 'display':fg(0)},
  173:{'c1':r158, 'c2':r159, 'display':fg(0)},
  174:{'c1':r159, 'c2':r160, 'display':fg(0)},
  175:{'c1':r160, 'c2':r161, 'display':fg(0)},
  176:{'c1':r160, 'c2':r162, 'display':fg(0)},
  177:{'c1':r162, 'c2':r163, 'display':fg(0)},
  178:{'c1':r163, 'c2':r164, 'display':fg(0)},
  179:{'c1':r164, 'c2':r165, 'display':fg(0)},
  180:{'c1':r164, 'c2':r166, 'display':fg(0)},
  181:{'c1':r166, 'c2':r167, 'display':fg(0)},
  182:{'c1':r167, 'c2':r168, 'display':fg(0)},
  183:{'c1':r31, 'c2':r40, 'display':fg(0)}}





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
  if rooms[Player.CRoom][dir] == r108 and items['Boat']['num'] == 0:
    print(fg(196)+'You need a boat to go any further')
    halt()
  else:  
    Player.PreRoom = Player.CRoom
    Player.CRoom = rooms[Player.CRoom][dir]
    rooms[Player.CRoom]['seen'] = 1
    for n in connect:
      if connect[n]['c1'] == Player.CRoom or connect[n]['c2'] == Player.CRoom:
        connect[n]['display'] = Fore.RESET


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
  inv('Spores (Scroll)')
  inv('Shroomal Sythe')
  inv('Food (Large)')
  inv('Heal Potion (Medium)')
  inv('Map (Crossroads)')
  inv('Half Plate')
  inv('Lightning Dagger')
  inv('Vine Wrap (Scroll)')
  inv('Fireball (Scroll)')
  inv('Staff of the Magi')
  inv('Grand Crown')
  inv('Waterfall (Scroll)')
  inv('Ocean Reaver')
  inv('Boat')
  inv('Map (Lagoon)')
  inv('Blunderbuss')
  inv('Cannonball')
  inv('Smite (Scroll)')
  inv('Scale Mail')



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
  if items['Ocean Reaver']['num'] != 0:
    print(Fore.GREEN + '                      (14)')
  inv('Ocean Reaver')
  if items['Blunderbuss']['num'] != 0:
    print(Fore.GREEN + '                      (15)')
  inv('Blunderbuss')
  if items['Scale Mail']['num'] != 0:
    print(Fore.GREEN + '                      (16)')
  inv('Scale Mail')



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
  if items['Smite (Scroll)']['num'] != 0:
    print(Fore.GREEN + '                      (11)')
  inv('Smite (Scroll)')




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
  if items['Smite (Scroll)']['num'] == 1 and 'Smite (Scroll)' in spList:
    print('Smite (11)')




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

def checkProxim(type,enemy,enemy2,enemy3,enemy4,radius,spell,colour):
  if radius == 1:
    if type == 2:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
    if type == 3:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile -1 or enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile +20 or enemy.ETile == enemy3.ETile -20 or enemy.ETile == enemy3.ETile +19 or enemy.ETile == enemy3.ETile -19 or enemy.ETile == enemy3.ETile +21 or enemy.ETile == enemy3.ETile -21:
        enemy3.H -= items[spell]['pow']
        screen[enemy3.ETile]['display'] = colour + '@@' + Fore.RESET
    if type == 4:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile -1 or enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile +20 or enemy.ETile == enemy3.ETile -20 or enemy.ETile == enemy3.ETile +19 or enemy.ETile == enemy3.ETile -19 or enemy.ETile == enemy3.ETile +21 or enemy.ETile == enemy3.ETile -21:
        enemy3.H -= items[spell]['pow']
        screen[enemy3.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy4.ETile +1 or enemy.ETile == enemy4.ETile -1 or enemy.ETile == enemy4.ETile +1 or enemy.ETile == enemy4.ETile +20 or enemy.ETile == enemy4.ETile -20 or enemy.ETile == enemy4.ETile +19 or enemy.ETile == enemy4.ETile -19 or enemy.ETile == enemy4.ETile +21 or enemy.ETile == enemy4.ETile -21:
        enemy4.H -= items[spell]['pow']
        screen[enemy4.ETile]['display'] = colour + '@@' + Fore.RESET

  if radius == 2:
    if type == 2:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21 or enemy.ETile == enemy2.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy2.ETile +22 or enemy.ETile == enemy2.ETile -22 or enemy.ETile == enemy2.ETile +18 or enemy.ETile == enemy2.ETile -18 or enemy.ETile == enemy2.ETile +40 or enemy.ETile == enemy2.ETile -40 or enemy.ETile == enemy2.ETile +41 or enemy.ETile == enemy2.ETile -41 or enemy.ETile == enemy2.ETile +39 or enemy.ETile == enemy2.ETile -39:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
    if type == 3:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21 or enemy.ETile == enemy2.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy2.ETile +22 or enemy.ETile == enemy2.ETile -22 or enemy.ETile == enemy2.ETile +18 or enemy.ETile == enemy2.ETile -18 or enemy.ETile == enemy2.ETile +40 or enemy.ETile == enemy2.ETile -40 or enemy.ETile == enemy2.ETile +41 or enemy.ETile == enemy2.ETile -41 or enemy.ETile == enemy2.ETile +39 or enemy.ETile == enemy2.ETile -39:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile -1 or enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile +20 or enemy.ETile == enemy3.ETile -20 or enemy.ETile == enemy3.ETile +19 or enemy.ETile == enemy3.ETile -19 or enemy.ETile == enemy3.ETile +21 or enemy.ETile == enemy3.ETile -21 or enemy.ETile == enemy3.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy3.ETile +22 or enemy.ETile == enemy3.ETile -22 or enemy.ETile == enemy3.ETile +18 or enemy.ETile == enemy3.ETile -18 or enemy.ETile == enemy3.ETile +40 or enemy.ETile == enemy3.ETile -40 or enemy.ETile == enemy3.ETile +41 or enemy.ETile == enemy3.ETile -41 or enemy.ETile == enemy3.ETile +39 or enemy.ETile == enemy3.ETile -39:
        enemy3.H -= items[spell]['pow']
        screen[enemy3.ETile]['display'] = colour + '@@' + Fore.RESET
    if type == 4:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21 or enemy.ETile == enemy2.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy2.ETile +22 or enemy.ETile == enemy2.ETile -22 or enemy.ETile == enemy2.ETile +18 or enemy.ETile == enemy2.ETile -18 or enemy.ETile == enemy2.ETile +40 or enemy.ETile == enemy2.ETile -40 or enemy.ETile == enemy2.ETile +41 or enemy.ETile == enemy2.ETile -41 or enemy.ETile == enemy2.ETile +39 or enemy.ETile == enemy2.ETile -39:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile -1 or enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile +20 or enemy.ETile == enemy3.ETile -20 or enemy.ETile == enemy3.ETile +19 or enemy.ETile == enemy3.ETile -19 or enemy.ETile == enemy3.ETile +21 or enemy.ETile == enemy3.ETile -21 or enemy.ETile == enemy3.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy3.ETile +22 or enemy.ETile == enemy3.ETile -22 or enemy.ETile == enemy3.ETile +18 or enemy.ETile == enemy3.ETile -18 or enemy.ETile == enemy3.ETile +40 or enemy.ETile == enemy3.ETile -40 or enemy.ETile == enemy3.ETile +41 or enemy.ETile == enemy3.ETile -41 or enemy.ETile == enemy3.ETile +39 or enemy.ETile == enemy3.ETile -39:
        enemy3.H -= items[spell]['pow']
        screen[enemy3.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy4.ETile +1 or enemy.ETile == enemy4.ETile -1 or enemy.ETile == enemy4.ETile +1 or enemy.ETile == enemy4.ETile +20 or enemy.ETile == enemy4.ETile -20 or enemy.ETile == enemy4.ETile +19 or enemy.ETile == enemy4.ETile -19 or enemy.ETile == enemy4.ETile +21 or enemy.ETile == enemy4.ETile -21 or enemy.ETile == enemy4.ETile +2 or enemy.ETile == enemy4.ETile -2 or enemy.ETile == enemy4.ETile +22 or enemy.ETile == enemy4.ETile -22 or enemy.ETile == enemy4.ETile +18 or enemy.ETile == enemy4.ETile -18 or enemy.ETile == enemy4.ETile +40 or enemy.ETile == enemy4.ETile -40 or enemy.ETile == enemy4.ETile +41 or enemy.ETile == enemy4.ETile -41 or enemy.ETile == enemy4.ETile +39 or enemy.ETile == enemy4.ETile -39:
        enemy4.H -= items[spell]['pow']
        screen[enemy4.ETile]['display'] = colour + '@@' + Fore.RESET

  if radius == 3:
    if type == 2:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21 or enemy.ETile == enemy2.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy2.ETile +22 or enemy.ETile == enemy2.ETile -22 or enemy.ETile == enemy2.ETile +18 or enemy.ETile == enemy2.ETile -18 or enemy.ETile == enemy2.ETile +40 or enemy.ETile == enemy2.ETile -40 or enemy.ETile == enemy2.ETile +41 or enemy.ETile == enemy2.ETile -41 or enemy.ETile == enemy2.ETile +39 or enemy.ETile == enemy2.ETile -39 or enemy.ETile == enemy2.ETile +3 or enemy.ETile == enemy2.ETile -3 or enemy.ETile == enemy2.ETile +23 or enemy.ETile == enemy2.ETile -23 or enemy.ETile == enemy2.ETile +17 or enemy.ETile == enemy2.ETile -17 or enemy.ETile == enemy2.ETile +60 or enemy.ETile == enemy2.ETile -60 or enemy.ETile == enemy2.ETile +61 or enemy.ETile == enemy2.ETile -61 or enemy.ETile == enemy2.ETile +59 or enemy.ETile == enemy2.ETile -59 or enemy.ETile == enemy2.ETile +42 or enemy.ETile == enemy2.ETile -42 or enemy.ETile == enemy2.ETile +38 or enemy.ETile == enemy2.ETile -38:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
    if type == 3:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21 or enemy.ETile == enemy2.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy2.ETile +22 or enemy.ETile == enemy2.ETile -22 or enemy.ETile == enemy2.ETile +18 or enemy.ETile == enemy2.ETile -18 or enemy.ETile == enemy2.ETile +40 or enemy.ETile == enemy2.ETile -40 or enemy.ETile == enemy2.ETile +41 or enemy.ETile == enemy2.ETile -41 or enemy.ETile == enemy2.ETile +39 or enemy.ETile == enemy2.ETile -39 or enemy.ETile == enemy2.ETile +3 or enemy.ETile == enemy2.ETile -3 or enemy.ETile == enemy2.ETile +23 or enemy.ETile == enemy2.ETile -23 or enemy.ETile == enemy2.ETile +17 or enemy.ETile == enemy2.ETile -17 or enemy.ETile == enemy2.ETile +60 or enemy.ETile == enemy2.ETile -60 or enemy.ETile == enemy2.ETile +61 or enemy.ETile == enemy2.ETile -61 or enemy.ETile == enemy2.ETile +59 or enemy.ETile == enemy2.ETile -59 or enemy.ETile == enemy2.ETile +42 or enemy.ETile == enemy2.ETile -42 or enemy.ETile == enemy2.ETile +38 or enemy.ETile == enemy2.ETile -38:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile -1 or enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile +20 or enemy.ETile == enemy3.ETile -20 or enemy.ETile == enemy3.ETile +19 or enemy.ETile == enemy3.ETile -19 or enemy.ETile == enemy3.ETile +21 or enemy.ETile == enemy3.ETile -21 or enemy.ETile == enemy3.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy3.ETile +22 or enemy.ETile == enemy3.ETile -22 or enemy.ETile == enemy3.ETile +18 or enemy.ETile == enemy3.ETile -18 or enemy.ETile == enemy3.ETile +40 or enemy.ETile == enemy3.ETile -40 or enemy.ETile == enemy3.ETile +41 or enemy.ETile == enemy3.ETile -41 or enemy.ETile == enemy3.ETile +39 or enemy.ETile == enemy3.ETile -39 or enemy.ETile == enemy3.ETile +3 or enemy.ETile == enemy3.ETile -3 or enemy.ETile == enemy3.ETile +23 or enemy.ETile == enemy3.ETile -23 or enemy.ETile == enemy3.ETile +17 or enemy.ETile == enemy3.ETile -17 or enemy.ETile == enemy3.ETile +60 or enemy.ETile == enemy3.ETile -60 or enemy.ETile == enemy3.ETile +61 or enemy.ETile == enemy3.ETile -61 or enemy.ETile == enemy3.ETile +59 or enemy.ETile == enemy3.ETile -59 or enemy.ETile == enemy3.ETile +42 or enemy.ETile == enemy3.ETile -42 or enemy.ETile == enemy3.ETile +38 or enemy.ETile == enemy3.ETile -38:
        enemy3.H -= items[spell]['pow']
        screen[enemy3.ETile]['display'] = colour + '@@' + Fore.RESET
    if type == 4:
      if enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile -1 or enemy.ETile == enemy2.ETile +1 or enemy.ETile == enemy2.ETile +20 or enemy.ETile == enemy2.ETile -20 or enemy.ETile == enemy2.ETile +19 or enemy.ETile == enemy2.ETile -19 or enemy.ETile == enemy2.ETile +21 or enemy.ETile == enemy2.ETile -21 or enemy.ETile == enemy2.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy2.ETile +22 or enemy.ETile == enemy2.ETile -22 or enemy.ETile == enemy2.ETile +18 or enemy.ETile == enemy2.ETile -18 or enemy.ETile == enemy2.ETile +40 or enemy.ETile == enemy2.ETile -40 or enemy.ETile == enemy2.ETile +41 or enemy.ETile == enemy2.ETile -41 or enemy.ETile == enemy2.ETile +39 or enemy.ETile == enemy2.ETile -39 or enemy.ETile == enemy2.ETile +3 or enemy.ETile == enemy2.ETile -3 or enemy.ETile == enemy2.ETile +23 or enemy.ETile == enemy2.ETile -23 or enemy.ETile == enemy2.ETile +17 or enemy.ETile == enemy2.ETile -17 or enemy.ETile == enemy2.ETile +60 or enemy.ETile == enemy2.ETile -60 or enemy.ETile == enemy2.ETile +61 or enemy.ETile == enemy2.ETile -61 or enemy.ETile == enemy2.ETile +59 or enemy.ETile == enemy2.ETile -59 or enemy.ETile == enemy2.ETile +42 or enemy.ETile == enemy2.ETile -42 or enemy.ETile == enemy2.ETile +38 or enemy.ETile == enemy2.ETile -38:
        enemy2.H -= items[spell]['pow']
        screen[enemy2.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile -1 or enemy.ETile == enemy3.ETile +1 or enemy.ETile == enemy3.ETile +20 or enemy.ETile == enemy3.ETile -20 or enemy.ETile == enemy3.ETile +19 or enemy.ETile == enemy3.ETile -19 or enemy.ETile == enemy3.ETile +21 or enemy.ETile == enemy3.ETile -21 or enemy.ETile == enemy3.ETile +2 or enemy.ETile == enemy2.ETile -2 or enemy.ETile == enemy3.ETile +22 or enemy.ETile == enemy3.ETile -22 or enemy.ETile == enemy3.ETile +18 or enemy.ETile == enemy3.ETile -18 or enemy.ETile == enemy3.ETile +40 or enemy.ETile == enemy3.ETile -40 or enemy.ETile == enemy3.ETile +41 or enemy.ETile == enemy3.ETile -41 or enemy.ETile == enemy3.ETile +39 or enemy.ETile == enemy3.ETile -39 or enemy.ETile == enemy3.ETile +3 or enemy.ETile == enemy3.ETile -3 or enemy.ETile == enemy3.ETile +23 or enemy.ETile == enemy3.ETile -23 or enemy.ETile == enemy3.ETile +17 or enemy.ETile == enemy3.ETile -17 or enemy.ETile == enemy3.ETile +60 or enemy.ETile == enemy3.ETile -60 or enemy.ETile == enemy3.ETile +61 or enemy.ETile == enemy3.ETile -61 or enemy.ETile == enemy3.ETile +59 or enemy.ETile == enemy3.ETile -59 or enemy.ETile == enemy3.ETile +42 or enemy.ETile == enemy3.ETile -42 or enemy.ETile == enemy3.ETile +38 or enemy.ETile == enemy3.ETile -38:
        enemy3.H -= items[spell]['pow']
        screen[enemy3.ETile]['display'] = colour + '@@' + Fore.RESET
      if enemy.ETile == enemy4.ETile +1 or enemy.ETile == enemy4.ETile -1 or enemy.ETile == enemy4.ETile +1 or enemy.ETile == enemy4.ETile +20 or enemy.ETile == enemy4.ETile -20 or enemy.ETile == enemy4.ETile +19 or enemy.ETile == enemy4.ETile -19 or enemy.ETile == enemy4.ETile +21 or enemy.ETile == enemy4.ETile -21 or enemy.ETile == enemy4.ETile +2 or enemy.ETile == enemy4.ETile -2 or enemy.ETile == enemy4.ETile +22 or enemy.ETile == enemy4.ETile -22 or enemy.ETile == enemy4.ETile +18 or enemy.ETile == enemy4.ETile -18 or enemy.ETile == enemy4.ETile +40 or enemy.ETile == enemy4.ETile -40 or enemy.ETile == enemy4.ETile +41 or enemy.ETile == enemy4.ETile -41 or enemy.ETile == enemy4.ETile +39 or enemy.ETile == enemy4.ETile -39 or enemy.ETile == enemy4.ETile +3 or enemy.ETile == enemy4.ETile -3 or enemy.ETile == enemy4.ETile +23 or enemy.ETile == enemy4.ETile -23 or enemy.ETile == enemy4.ETile +17 or enemy.ETile == enemy4.ETile -17 or enemy.ETile == enemy4.ETile +60 or enemy.ETile == enemy4.ETile -60 or enemy.ETile == enemy4.ETile +61 or enemy.ETile == enemy4.ETile -61 or enemy.ETile == enemy4.ETile +59 or enemy.ETile == enemy4.ETile -59 or enemy.ETile == enemy4.ETile +42 or enemy.ETile == enemy4.ETile -42 or enemy.ETile == enemy4.ETile +38 or enemy.ETile == enemy4.ETile -38:
        enemy4.H -= items[spell]['pow']
        screen[enemy4.ETile]['display'] = colour + '@@' + Fore.RESET


def spellAttack(enemy,com,type,enemy2,enemy3,enemy4):
  if items['Freeze Mist (Scroll)']['num'] == 1 and com == '1' and Player.SP != 0  and 'Freeze Mist (Scroll)' in spList:
    enemy.H -= items['Freeze Mist (Scroll)']['pow']
    screen[enemy.ETile]['display'] = fg(81) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Freeze Mist (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Lava Splash (Scroll)']['num'] == 1 and com == '2'and Player.SP != 0 and 'Lava Splash (Scroll)' in spList:
    enemy.H -= items['Lava Splash (Scroll)']['pow']
    checkProxim(type,enemy,enemy2,enemy3,enemy4,items['Lava Splash (Scroll)']['rad'],'Lava Splash (Scroll)', fg(160))
    screen[enemy.ETile]['display'] = fg(160) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Lava Splash (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Fire Bolt (Scroll)']['num'] == 1 and com == '3'and Player.SP != 0 and 'Fire Bolt (Scroll)' in spList:
    enemy.H -= items['Fire Bolt (Scroll)']['pow']
    screen[enemy.ETile]['display'] = fg(202) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Fire Bolt (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Tesla Coil (Scroll)']['num'] == 1 and com == '4'and Player.SP != 0 and 'Tesla Coil (Scroll)' in spList:
    enemy.H -= items['Tesla Coil (Scroll)']['pow']
    screen[enemy.ETile]['display'] = fg(39) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Tesla Coil (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Acid Bullet (Scroll)']['num'] == 1 and com == '5'and Player.SP != 0 and 'Acid Bullet (Scroll)' in spList:
    enemy.H -= items['Acid Bullet (Scroll)']['pow']
    screen[enemy.ETile]['display'] = fg(28) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Acid Bullet (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Web (Scroll)']['num'] == 1 and com == '6'and Player.SP != 0 and 'Web (Scroll)' in spList:
    enemy.H -= items['Web (Scroll)']['pow']
    checkProxim(type,enemy,enemy2,enemy3,enemy4,items['Web (Scroll)']['rad'],'Web (Scroll)', Fore.WHITE)
    screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Web (Scroll)']['pow']) + ' and the enemy has been stuck for 3 turns!')
    enemy.WTimer += 4
    Player.SP -= 1
    halt()
  elif items['Spores (Scroll)']['num'] == 1 and com == '7'and Player.SP != 0 and 'Spores (Scroll)' in spList:
    enemy.H -= items['Spores (Scroll)']['pow']
    checkProxim(type,enemy,enemy2,enemy3,enemy4,items['Spores (Scroll)']['rad'],'Spores (Scroll)', fg(43))
    screen[enemy.ETile]['display'] = fg(43) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Spores (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Vine Wrap (Scroll)']['num'] == 1 and com == '8'and Player.SP != 0 and 'Vine Wrap (Scroll)' in spList:
    enemy.H -= items['Vine Wrap (Scroll)']['pow']
    screen[enemy.ETile]['display'] = fg(70) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Vine Wrap (Scroll)']['pow'])+ ' and the enemy has been grappled for 1 turn!')
    enemy.WTimer += 2
    Player.SP -= 1
    halt()
  elif items['Fireball (Scroll)']['num'] == 1 and com == '9'and Player.SP != 0 and 'Fireball (Scroll)' in spList:
    enemy.H -= items['Fireball (Scroll)']['pow']
    checkProxim(type,enemy,enemy2,enemy3,enemy4,items['Fireball (Scroll)']['rad'],'Fireball (Scroll)', fg(202))
    screen[enemy.ETile]['display'] = fg(202) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Fireball (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Waterfall (Scroll)']['num'] == 1 and com == '10'and Player.SP != 0 and 'Waterfall (Scroll)' in spList:
    enemy.H -= items['Waterfall (Scroll)']['pow']
    screen[enemy.ETile]['display'] = fg(21) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
    print('The spell hits for ' + str(items['Waterfall (Scroll)']['pow']))
    Player.SP -= 1
    halt()
  elif items['Smite (Scroll)']['num'] == 1 and com == '11'and Player.SP != 0 and 'Smite (Scroll)' in spList:
    if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
      enemy.H -= items['Smite (Scroll)']['pow'] + items[Player.weapon]['pow']
      checkProxim(type,enemy,enemy2,enemy3,enemy4,items['Smite (Scroll)']['rad'],'Smite (Scroll)',fg(190))
      screen[enemy.ETile]['display'] = fg(190) + '@@' + Fore.RESET
      os.system('cls')
      print(Fore.BLUE + '--Player Turn--')
      battlemap()
      print('The spell hits for ' + str(items['Smite (Scroll)']['pow'] + items[Player.weapon]['pow']))
      Player.SP -= 1
      halt()
    else:
      print('not an option')
      halt()

  else:
    print('not an option')
    halt()


def playerHeal():
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
  elif com == '2' and items['Food (Medium)']['num'] > 0:
    items['Food (Medium)']['num'] -= 1
    Player.H += items['Food (Medium)']['heal']
    if Player.H >= 100:
      Player.H = 100
      print(Fore.GREEN + 'Healed to full!')
    else:
      print('Healed ' + str(items['Food (Medium)']['heal']))
    halt()
  elif com == '3' and items['Food (Large)']['num'] > 0:
    items['Food (Large)']['num'] -= 1
    Player.H += items['Food (Large)']['heal']
    if Player.H >= 100:
      Player.H = 100
      print(Fore.GREEN + 'Healed to full!')
    else:
      print('Healed ' + str(items['Food (Large)']['heal']))
    halt()
  elif com == '4' and items['Heal Potion (Small)']['num'] > 0:
    items['Heal Potion (Small)']['num'] -= 1
    Player.H += items['Heal Potion (Small)']['heal']
    if Player.H >= 100:
      Player.H = 100
      print(Fore.GREEN + 'Healed to full!')
    else:
      print('Healed ' + str(items['Heal Potion (Small)']['heal']))
    halt()
  elif com == '5' and items['Heal Potion (Medium)']['num'] > 0:
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


def colour(enemy):
  if items[Player.weapon]['type'] == 'blunt':
    screen[enemy.ETile]['display'] = fg(242) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
  elif items[Player.weapon]['type'] == 'slash':
    screen[enemy.ETile]['display'] = fg(116) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
  elif items[Player.weapon]['type'] == 'acid':
    screen[enemy.ETile]['display'] = fg(28) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
  elif items[Player.weapon]['type'] == 'shock':
    screen[enemy.ETile]['display'] = fg(39) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()
  elif items[Player.weapon]['type'] == 'water':
    screen[enemy.ETile]['display'] = fg(21) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()      
  elif items[Player.weapon]['type'] == 'pierce':
    screen[enemy.ETile]['display'] = fg(189) + '@@' + Fore.RESET
    os.system('cls')
    print(Fore.BLUE + '--Player Turn--')
    battlemap()






def fight1(enemy):
  screen[Player.CTile]['display'] = '  '
  Player.CTile = enemy.STile
  for n in screen:
    screen[n]['display'] = '  '
  x = 0
  while x == 0:
    for n in screen:
      if rooms[Player.CRoom]['bmap'][screen[n]['y']][screen[n]['x']] == 1:
        screen[n]['display'] = '##'
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if enemy.WTimer != 0:
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
    if enemy.WTimer != 0:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@@' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
    i = 0
    while i == 0:
      os.system('cls')
      print(Fore.BLUE + '--Player Turn--')
      battlemap()
      print(Fore.RED + 'Player Health = ' + str(Player.H) )
      print(Fore.BLUE + 'Player SP = ' + str(Player.SP) + Fore.RESET)
      print(Fore.RED + 'Enemy Health = ' + str(enemy.H))
      print(Fore.RESET + '\n\n\n')
      print('Your turn, options are:\n'+Fore.BLUE+'Flee (f)\nSpell (q)\nItem (e)\nSprint (s)\nNothing (ENTER)')
      if  Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
        print('Attack (m1)')
      com = input()
      if com == 's':
        playerMove()
        i = 1
      elif com == 'm1' and Player.CTile == enemy.ETile + 20 or com == 'm1' and Player.CTile == enemy.ETile - 20 or com == 'm1' and Player.CTile == enemy.ETile + 1 or com == 'm1' and Player.CTile == enemy.ETile - 1 or com == 'm1' and Player.CTile == enemy.ETile +21 or com == 'm1' and Player.CTile == enemy.ETile -21 or com == 'm1' and Player.CTile == enemy.ETile +19 or com == 'm1' and Player.CTile == enemy.ETile -19:
        enemy.H -= items[Player.weapon]['pow']
        colour(enemy)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1
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
        i = 1
      elif com == 'q':
        os.system('cls')
        print(Fore.GREEN + 'Your spells are:\n')
        spells()
        com = input('\n\nWhich spell do you cast?')
        spellAttack(enemy,com,1,enemy,enemy,enemy)
        i = 1
      elif com == 'e':
        playerHeal()
        i = 1
      elif com == '':
        i = 1
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
      if enemy.WTimer == 0:
        s = enemy.ESpeed
        while s >= 1:
          if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
            s = 0
          else:
            screen[enemy.ETile]['display'] = '  ' 
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy.ETile]['y'],screen[enemy.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy, 1, enemy, enemy, enemy)
            screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY MOVMENT--')
            battlemap()
            halt() 
          s -= 1 
        screen[enemy.ETile]['display'] = Fore.RED + '@@' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'The enemy is stuck!')
        enemy.WTimer -= 1
      if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
        print(Fore.RED + '--ENEMY TURN--')
        battlemap()
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
  screen[Player.CTile]['display'] = '  '
  Player.CTile = enemy.STile
  for n in screen:
    screen[n]['display'] = '  '
  x = 0
  while x == 0:
    for n in screen:
      if rooms[Player.CRoom]['bmap'][screen[n]['y']][screen[n]['x']] == 1:
        screen[n]['display'] = '##'
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET

    if enemy.WTimer != 0 and enemy.DTXT == False:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@1' + Fore.RESET
    elif enemy.DTXT == True:
      screen[enemy.ETile]['display'] = fg(236) + '@1' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET

    if enemy2.WTimer != 0 and enemy2.DTXT == False:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@2' + Fore.RESET
    elif enemy2.DTXT == True:
      screen[enemy2.ETile]['display'] = fg(236) + '@2' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET




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
    if enemy.WTimer != 0 and enemy.DTXT == False:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@1' + Fore.RESET
    elif enemy.DTXT == True:
      screen[enemy.ETile]['display'] = fg(236) + '@1' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET

    if enemy2.WTimer != 0 and enemy2.DTXT == False:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@2' + Fore.RESET
    elif enemy2.DTXT == True:
      screen[enemy2.ETile]['display'] = fg(236) + '@2' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
    i = 0
    while i == 0:
      os.system('cls')
      print(Fore.BLUE + '--Player Turn--')
      battlemap()
      print(Fore.RED + 'Player Health = ' + str(Player.H) )
      print(Fore.BLUE + 'Player SP = ' + str(Player.SP) + Fore.RESET)
      print(Fore.RED + '\nEnemy 1 Health = ' + str(enemy.H))
      print(Fore.RED + '\nEnemy 2 Health = ' + str(enemy2.H))
      print(Fore.RESET + '\n\n\n')
      print('Your turn, options are:\n'+Fore.BLUE+'Flee (f)\nSpell (q)\nItem (e)\nSprint (s)\nNothing (ENTER)')
      if enemy.DTXT == False:
        if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
          print('Attack Enemy 1 (m1)')
      if enemy2.DTXT == False:
        if  Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
          print('Attack Enemy 2 (m2)')
      com = input()


      if com == 's':
        playerMove()
        i = 1

      elif com == 'm1' and Player.CTile == enemy.ETile + 20 or com == 'm1' and Player.CTile == enemy.ETile - 20 or com == 'm1' and Player.CTile == enemy.ETile + 1 or com == 'm1' and Player.CTile == enemy.ETile - 1 or com == 'm1' and Player.CTile == enemy.ETile +21 or com == 'm1' and Player.CTile == enemy.ETile -21 or com == 'm1' and Player.CTile == enemy.ETile +19 or com == 'm1' and Player.CTile == enemy.ETile -19:
        enemy.H -= items[Player.weapon]['pow']
        colour(enemy)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

      elif com == 'm2' and Player.CTile == enemy2.ETile + 20 or com == 'm2' and Player.CTile == enemy2.ETile - 20 or com == 'm2' and Player.CTile == enemy2.ETile + 1 or com == 'm2' and Player.CTile == enemy2.ETile - 1 or com == 'm2' and Player.CTile == enemy2.ETile +21 or com == 'm2' and Player.CTile == enemy2.ETile -21 or com == 'm2' and Player.CTile == enemy2.ETile +19 or com == 'm2' and Player.CTile == enemy2.ETile -19:
        enemy2.H -= items[Player.weapon]['pow']
        colour(enemy2)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

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
        i = 1
      elif com == 'q':
        os.system('cls')
        if enemy.down == 0 and enemy2.down == 0: 
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,2,enemy2,enemy2,enemy2)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,2,enemy,enemy,enemy)
          else:
            print('Not an option')
            halt()
        elif enemy.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy2,com,1,enemy2,enemy2,enemy2)
        elif enemy2.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy,com,1,enemy2,enemy2,enemy2)
        i = 1
      elif com == 'e':
        playerHeal()
        i = 1
      elif com == '':
        i = 1
      else:
        print('not an option')
        halt()


    if enemy.H <= 0 and enemy.DTXT == False:
      os.system('cls')
      print('Enemy 1 dies!')
      halt()
      screen[enemy.ETile]['display'] = '  '
      enemy.down = 1
      enemy.DTXT = True

    if enemy2.H <= 0 and enemy2.DTXT == False:
      os.system('cls')
      print('Enemy 2 dies!')
      halt()
      screen[enemy2.ETile]['display'] = '  '
      enemy2.down = 1
      enemy2.DTXT = True

    if enemy.down == 1 and enemy2.down == 1:
      os.system('cls')
      print('The Enemies are defeated!')
      halt()
      x = 1



    os.system('cls')
    if enemy.down == 0:
      if enemy.WTimer == 0:
        s = enemy.ESpeed
        while s >= 1:
          if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
            s = 0
          else:
            screen[enemy.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy.ETile]['y'],screen[enemy.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy, 2, enemy2, enemy2, enemy2)
            screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 1 MOVMENT--')
            battlemap()
            halt()
          s -= 1  
        screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 1 is stuck!')
        enemy.WTimer -= 1

      if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
        print(Fore.RED + '--ENEMY 1 TURN--')
        battlemap()
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 1 misses!')
        else:
          print(Fore.RED + 'Enemy 1 hits for ' + str(enemy.damage))
          Player.H -= enemy.damage
        print(Fore.RESET)
        halt()
    if enemy2.down == 0:
      if enemy2.WTimer == 0:
        s = enemy2.ESpeed
        while s >= 1:
          if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
            s = 0
          else:
            screen[enemy2.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy2.ETile]['y'],screen[enemy2.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy2, 2, enemy, enemy, enemy)
            screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 2 MOVMENT--')
            battlemap()
            halt()
          s -= 1  
        screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 2 is stuck!')
        enemy2.WTimer -= 1

      if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
        print(Fore.RED + '--ENEMY 2 TURN--')
        battlemap()        
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



def fight3(enemy,enemy2,enemy3):
  screen[Player.CTile]['display'] = '  '
  Player.CTile = enemy.STile
  for n in screen:
    screen[n]['display'] = '  '
  x = 0
  while x == 0:
    for n in screen:
      if rooms[Player.CRoom]['bmap'][screen[n]['y']][screen[n]['x']] == 1:
        screen[n]['display'] = '##'
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET

    if enemy.WTimer != 0 and enemy.DTXT == False:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@1' + Fore.RESET
    elif enemy.DTXT == True:
      screen[enemy.ETile]['display'] = fg(236) + '@1' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET

    if enemy2.WTimer != 0 and enemy2.DTXT == False:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@2' + Fore.RESET
    elif enemy2.DTXT == True:
      screen[enemy2.ETile]['display'] = fg(236) + '@2' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET

    if enemy3.WTimer != 0 and enemy3.DTXT == False:
      screen[enemy3.ETile]['display'] = Fore.WHITE + '@3' + Fore.RESET
    elif enemy3.DTXT == True:
      screen[enemy3.ETile]['display'] = fg(236) + '@3' + Fore.RESET
    else:
      screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET



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
    enemy3.Ex = screen[enemy3.ETile]['x']
    enemy3.Ey = screen[enemy3.ETile]['y']
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if enemy.WTimer != 0 and enemy.DTXT == False:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@1' + Fore.RESET
    elif enemy.DTXT == True:
      screen[enemy.ETile]['display'] = fg(236) + '@1' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET

    if enemy2.WTimer != 0 and enemy2.DTXT == False:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@2' + Fore.RESET
    elif enemy2.DTXT == True:
      screen[enemy2.ETile]['display'] = fg(236) + '@2' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET

    if enemy3.WTimer != 0 and enemy3.DTXT == False:
      screen[enemy3.ETile]['display'] = Fore.WHITE + '@3' + Fore.RESET
    elif enemy3.DTXT == True:
      screen[enemy3.ETile]['display'] = fg(236) + '@3' + Fore.RESET
    else:
      screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET
    i = 0
    while i == 0:
      os.system('cls')
      print(Fore.BLUE + '--Player Turn--')
      battlemap()
      print(Fore.RED + 'Player Health = ' + str(Player.H) )
      print(Fore.BLUE + 'Player SP = ' + str(Player.SP) + Fore.RESET)
      print(Fore.RED + '\nEnemy 1 Health = ' + str(enemy.H))
      print(Fore.RED + '\nEnemy 2 Health = ' + str(enemy2.H))
      print(Fore.RED + '\nEnemy 3 Health = ' + str(enemy3.H))
      print(Fore.RESET + '\n\n\n')
      print('Your turn, options are:\n'+Fore.BLUE+'Flee (f)\nSpell (q)\nItem (e)\nSprint (s)\nNothing (ENTER)')
      if enemy.DTXT == False:
        if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
          print('Attack Enemy 1 (m1)')
      if enemy2.DTXT == False:
        if  Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
          print('Attack Enemy 2 (m2)')
      if enemy3.DTXT == False:
        if  Player.CTile == enemy3.ETile + 20 or Player.CTile == enemy3.ETile - 20 or Player.CTile == enemy3.ETile + 1 or Player.CTile == enemy3.ETile - 1 or Player.CTile == enemy3.ETile +21 or Player.CTile == enemy3.ETile -21 or Player.CTile == enemy3.ETile +19 or Player.CTile == enemy3.ETile -19:
          print('Attack Enemy 3 (m3)')
      com = input()


      if com == 's':
        playerMove()
        i = 1

      elif com == 'm1' and Player.CTile == enemy.ETile + 20 or com == 'm1' and Player.CTile == enemy.ETile - 20 or com == 'm1' and Player.CTile == enemy.ETile + 1 or com == 'm1' and Player.CTile == enemy.ETile - 1 or com == 'm1' and Player.CTile == enemy.ETile +21 or com == 'm1' and Player.CTile == enemy.ETile -21 or com == 'm1' and Player.CTile == enemy.ETile +19 or com == 'm1' and Player.CTile == enemy.ETile -19:
        enemy.H -= items[Player.weapon]['pow']
        colour(enemy)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

      elif com == 'm2' and Player.CTile == enemy2.ETile + 20 or com == 'm2' and Player.CTile == enemy2.ETile - 20 or com == 'm2' and Player.CTile == enemy2.ETile + 1 or com == 'm2' and Player.CTile == enemy2.ETile - 1 or com == 'm2' and Player.CTile == enemy2.ETile +21 or com == 'm2' and Player.CTile == enemy2.ETile -21 or com == 'm2' and Player.CTile == enemy2.ETile +19 or com == 'm2' and Player.CTile == enemy2.ETile -19:
        enemy2.H -= items[Player.weapon]['pow']
        colour(enemy2)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

      elif com == 'm3' and Player.CTile == enemy3.ETile + 20 or com == 'm3' and Player.CTile == enemy3.ETile - 20 or com == 'm3' and Player.CTile == enemy3.ETile + 1 or com == 'm3' and Player.CTile == enemy3.ETile - 1 or com == 'm3' and Player.CTile == enemy3.ETile +21 or com == 'm3' and Player.CTile == enemy3.ETile -21 or com == 'm3' and Player.CTile == enemy3.ETile +19 or com == 'm3' and Player.CTile == enemy3.ETile -19:
        enemy3.H -= items[Player.weapon]['pow']
        colour(enemy3)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

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
        i = 1
      elif com == 'q':
        os.system('cls')

        if enemy.down == 0 and enemy2.down == 0 and enemy3.down == 0:
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)          Enemy3  (3)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,3,enemy2,enemy3,enemy)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,3,enemy,enemy3,enemy3)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,3,enemy,enemy2,enemy2)
          else:
            print('Not an option')
            halt()      

        elif enemy.down == 1 and enemy2.down == 0 and enemy3.down == 0: 
          os.system('cls')
          print('Enemy 2  (2)          Enemy3  (3)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,2,enemy3,enemy3,enemy3)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,2,enemy2,enemy2,enemy2)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 0 and enemy2.down == 1 and enemy3.down == 0: 
          os.system('cls')
          print('Enemy 1  (1)          Enemy3  (3)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,2,enemy3,enemy3,enemy3)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,2,enemy,enemy,enemy)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 0 and enemy2.down == 0 and enemy3.down == 1: 
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,2,enemy2,enemy2,enemy2)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,2,enemy,enemy,enemy)
          else:
            print('Not an option')
            halt()

        elif enemy2.down == 1 and enemy3.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy,com,1,enemy,enemy,enemy)

        elif enemy.down == 1 and enemy3.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy2,com,1,enemy2,enemy2,enemy2)

        elif enemy.down == 1 and enemy2.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy3,com,1,enemy3,enemy3,enemy3)
        i = 1
      elif com == 'e':
        playerHeal()
        i = 1
      elif com == '':
        i = 1
      
      else:
        print('not an option')
        halt()


    if enemy.H <= 0 and enemy.DTXT == False:
      os.system('cls')
      print('Enemy 1 dies!')
      halt()
      screen[enemy.ETile]['display'] = '  '
      enemy.down = 1
      enemy.DTXT = True

    if enemy2.H <= 0 and enemy2.DTXT == False:
      os.system('cls')
      print('Enemy 2 dies!')
      halt()
      screen[enemy2.ETile]['display'] = '  '
      enemy2.down = 1
      enemy2.DTXT = True

    if enemy3.H <= 0 and enemy3.DTXT == False:
      os.system('cls')
      print('Enemy 3 dies!')
      halt()
      screen[enemy3.ETile]['display'] = fg(236) + '@@'
      enemy3.down = 1
      enemy3.DTXT = True

    if enemy.down == 1 and enemy2.down == 1 and enemy3.down == 1:
      os.system('cls')
      print('The Enemies are defeated!')
      halt()
      x = 1



    os.system('cls')
    if enemy.down == 0:
      if enemy.WTimer == 0:
        s = enemy.ESpeed
        while s >= 1:
          if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
            s = 0
          else:
            screen[enemy.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy.ETile]['y'],screen[enemy.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy, 3, enemy2, enemy3, enemy3)
            screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 1 MOVMENT--')
            battlemap()
            halt()          
          s -= 1  
        screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 1 is stuck!')
        enemy.WTimer -= 1

      if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
        print(Fore.RED + '--ENEMY 1 TURN--')
        battlemap()
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 1 misses!')
        else:
          print(Fore.RED + 'Enemy 1 hits for ' + str(enemy.damage))
          Player.H -= enemy.damage
        print(Fore.RESET)
        halt()
    if enemy2.down == 0:
      if enemy2.WTimer == 0:
        s = enemy2.ESpeed
        while s >= 1:
          if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
            s = 0
          else:
            screen[enemy2.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy2.ETile]['y'],screen[enemy2.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy2, 3, enemy, enemy3, enemy3)
            screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 2 MOVMENT--')
            battlemap()
            halt()         
          s -= 1  
        screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 2 is stuck!')
        enemy2.WTimer -= 1

      if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
        print(Fore.RED + '--ENEMY 2 TURN--')
        battlemap()        
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 2 misses!')
        else:
          print(Fore.RED + 'Enemy 2 hits for ' + str(enemy2.damage))
          Player.H -= enemy2.damage
        print(Fore.RESET)
        halt()
    if enemy3.down == 0:
      if enemy3.WTimer == 0:
        s = enemy3.ESpeed
        while s >= 1:
          if Player.CTile == enemy3.ETile + 20 or Player.CTile == enemy3.ETile - 20 or Player.CTile == enemy3.ETile + 1 or Player.CTile == enemy3.ETile - 1 or Player.CTile == enemy3.ETile +21 or Player.CTile == enemy3.ETile -21 or Player.CTile == enemy3.ETile +19 or Player.CTile == enemy3.ETile -19:
            s = 0
          else:
            screen[enemy3.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy3.ETile]['y'],screen[enemy3.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy3, 3, enemy, enemy2, enemy2)
            screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 3 MOVMENT--')
            battlemap()
            halt()          
          s -= 1  
        screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 3 is stuck!')
        enemy3.WTimer -= 1

      if Player.CTile == enemy3.ETile + 20 or Player.CTile == enemy3.ETile - 20 or Player.CTile == enemy3.ETile + 1 or Player.CTile == enemy3.ETile - 1 or Player.CTile == enemy3.ETile +21 or Player.CTile == enemy3.ETile -21 or Player.CTile == enemy3.ETile +19 or Player.CTile == enemy3.ETile -19:
        print(Fore.RED + '--ENEMY 3 TURN--')
        battlemap()        
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 3 misses!')
        else:
          print(Fore.RED + 'Enemy 3 hits for ' + str(enemy3.damage))
          Player.H -= enemy3.damage
        print(Fore.RESET)
        halt()

    os.system('cls')
    if Player.H <= 0:
      os.system('cls')
      print('You Died!')
      halt()
      x = 1



def fight4(enemy,enemy2,enemy3,enemy4):
  screen[Player.CTile]['display'] = '  '
  Player.CTile = enemy.STile
  for n in screen:
    screen[n]['display'] = '  '
  x = 0
  while x == 0:
    for n in screen:
      if rooms[Player.CRoom]['bmap'][screen[n]['y']][screen[n]['x']] == 1:
        screen[n]['display'] = '##'
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET

    if enemy.WTimer != 0 and enemy.DTXT == False:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@1' + Fore.RESET
    elif enemy.DTXT == True:
      screen[enemy.ETile]['display'] = fg(236) + '@1' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET

    if enemy2.WTimer != 0 and enemy2.DTXT == False:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@2' + Fore.RESET
    elif enemy2.DTXT == True:
      screen[enemy2.ETile]['display'] = fg(236) + '@2' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET

    if enemy3.WTimer != 0 and enemy3.DTXT == False:
      screen[enemy3.ETile]['display'] = Fore.WHITE + '@3' + Fore.RESET
    elif enemy3.DTXT == True:
      screen[enemy3.ETile]['display'] = fg(236) + '@3' + Fore.RESET
    else:
      screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET

    if enemy4.WTimer != 0 and enemy4.DTXT == False:
      screen[enemy4.ETile]['display'] = Fore.WHITE + '@4' + Fore.RESET
    elif enemy4.DTXT == True:
      screen[enemy4.ETile]['display'] = fg(236) + '@4' + Fore.RESET
    else:
      screen[enemy4.ETile]['display'] = Fore.RED + '@4' + Fore.RESET

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
    enemy3.Ex = screen[enemy3.ETile]['x']
    enemy3.Ey = screen[enemy3.ETile]['y']
    enemy4.Ex = screen[enemy4.ETile]['x']
    enemy4.Ey = screen[enemy4.ETile]['y']
    screen[Player.CTile]['display'] = Fore.GREEN + '@@' + Fore.RESET
    if enemy.WTimer != 0 and enemy.DTXT == False:
      screen[enemy.ETile]['display'] = Fore.WHITE + '@1' + Fore.RESET
    elif enemy.DTXT == True:
      screen[enemy.ETile]['display'] = fg(236) + '@1' + Fore.RESET
    else:
      screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET

    if enemy2.WTimer != 0 and enemy2.DTXT == False:
      screen[enemy2.ETile]['display'] = Fore.WHITE + '@2' + Fore.RESET
    elif enemy2.DTXT == True:
      screen[enemy2.ETile]['display'] = fg(236) + '@2' + Fore.RESET
    else:
      screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET

    if enemy3.WTimer != 0 and enemy3.DTXT == False:
      screen[enemy3.ETile]['display'] = Fore.WHITE + '@3' + Fore.RESET
    elif enemy3.DTXT == True:
      screen[enemy3.ETile]['display'] = fg(236) + '@3' + Fore.RESET
    else:
      screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET

    if enemy4.WTimer != 0 and enemy4.DTXT == False:
      screen[enemy4.ETile]['display'] = Fore.WHITE + '@4' + Fore.RESET
    elif enemy4.DTXT == True:
      screen[enemy4.ETile]['display'] = fg(236) + '@4' + Fore.RESET
    else:
      screen[enemy4.ETile]['display'] = Fore.RED + '@4' + Fore.RESET
    i = 0
    while i == 0:
      os.system('cls')
      print(Fore.BLUE + '--Player Turn--')
      battlemap()
      print(Fore.RED + 'Player Health = ' + str(Player.H) )
      print(Fore.BLUE + 'Player SP = ' + str(Player.SP) + Fore.RESET)
      print(Fore.RED + '\nEnemy 1 Health = ' + str(enemy.H))
      print(Fore.RED + '\nEnemy 2 Health = ' + str(enemy2.H))
      print(Fore.RED + '\nEnemy 3 Health = ' + str(enemy3.H))
      print(Fore.RED + '\nEnemy 4 Health = ' + str(enemy4.H))    
      print(Fore.RESET + '\n\n\n')
      print('Your turn, options are:\n'+Fore.BLUE+'Flee (f)\nSpell (q)\nItem (e)\nSprint (s)\nNothing (ENTER)')
      if enemy.DTXT == False:
        if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
          print('Attack Enemy 1 (m1)')
      if enemy2.DTXT == False:
        if  Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
          print('Attack Enemy 2 (m2)')
      if enemy3.DTXT == False:
        if  Player.CTile == enemy3.ETile + 20 or Player.CTile == enemy3.ETile - 20 or Player.CTile == enemy3.ETile + 1 or Player.CTile == enemy3.ETile - 1 or Player.CTile == enemy3.ETile +21 or Player.CTile == enemy3.ETile -21 or Player.CTile == enemy3.ETile +19 or Player.CTile == enemy3.ETile -19:
          print('Attack Enemy 3 (m3)')
      if enemy4.DTXT == False:
        if  Player.CTile == enemy4.ETile + 20 or Player.CTile == enemy4.ETile - 20 or Player.CTile == enemy4.ETile + 1 or Player.CTile == enemy4.ETile - 1 or Player.CTile == enemy4.ETile +21 or Player.CTile == enemy4.ETile -21 or Player.CTile == enemy4.ETile +19 or Player.CTile == enemy4.ETile -19:
          print('Attack Enemy 4 (m4)')
      com = input()


      if com == 's':
        playerMove()
        i = 1

      elif com == 'm1' and Player.CTile == enemy.ETile + 20 or com == 'm1' and Player.CTile == enemy.ETile - 20 or com == 'm1' and Player.CTile == enemy.ETile + 1 or com == 'm1' and Player.CTile == enemy.ETile - 1 or com == 'm1' and Player.CTile == enemy.ETile +21 or com == 'm1' and Player.CTile == enemy.ETile -21 or com == 'm1' and Player.CTile == enemy.ETile +19 or com == 'm1' and Player.CTile == enemy.ETile -19:
        enemy.H -= items[Player.weapon]['pow']
        colour(enemy)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

      elif com == 'm2' and Player.CTile == enemy2.ETile + 20 or com == 'm2' and Player.CTile == enemy2.ETile - 20 or com == 'm2' and Player.CTile == enemy2.ETile + 1 or com == 'm2' and Player.CTile == enemy2.ETile - 1 or com == 'm2' and Player.CTile == enemy2.ETile +21 or com == 'm2' and Player.CTile == enemy2.ETile -21 or com == 'm2' and Player.CTile == enemy2.ETile +19 or com == 'm2' and Player.CTile == enemy2.ETile -19:
        enemy2.H -= items[Player.weapon]['pow']
        colour(enemy2)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

      elif com == 'm3' and Player.CTile == enemy3.ETile + 20 or com == 'm3' and Player.CTile == enemy3.ETile - 20 or com == 'm3' and Player.CTile == enemy3.ETile + 1 or com == 'm3' and Player.CTile == enemy3.ETile - 1 or com == 'm3' and Player.CTile == enemy3.ETile +21 or com == 'm3' and Player.CTile == enemy3.ETile -21 or com == 'm3' and Player.CTile == enemy3.ETile +19 or com == 'm3' and Player.CTile == enemy3.ETile -19:
        enemy3.H -= items[Player.weapon]['pow']
        colour(enemy3)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

      elif com == 'm4' and Player.CTile == enemy4.ETile + 20 or com == 'm4' and Player.CTile == enemy4.ETile - 20 or com == 'm4' and Player.CTile == enemy4.ETile + 1 or com == 'm4' and Player.CTile == enemy4.ETile - 1 or com == 'm4' and Player.CTile == enemy4.ETile +21 or com == 'm4' and Player.CTile == enemy4.ETile -21 or com == 'm4' and Player.CTile == enemy4.ETile +19 or com == 'm4' and Player.CTile == enemy4.ETile -19:
        enemy4.H -= items[Player.weapon]['pow']
        colour(enemy4)
        print('Hits for  ' + str(items[Player.weapon]['pow']))
        halt()
        i = 1

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
        i = 1
      elif com == 'q':
        os.system('cls')



        if enemy.down == 0 and enemy2.down == 0 and enemy3.down == 0 and enemy4.down == 0:
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)          Enemy3  (3)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,4,enemy2,enemy3,enemy4)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,4,enemy,enemy3,enemy4)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,4,enemy,enemy2,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,4,enemy,enemy2,enemy3) 
          else:
            print('Not an option')
            halt()        
        elif enemy.down == 0 and enemy2.down == 0 and enemy3.down == 0 and enemy4.down == 1:
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)          Enemy3  (3)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,3,enemy2,enemy3,enemy3)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,3,enemy,enemy3,enemy3)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,3,enemy,enemy2,enemy2) 
          else:
            print('Not an option')
            halt()        
        elif enemy.down == 0 and enemy2.down == 0 and enemy3.down == 1 and enemy4.down == 0:
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,3,enemy2,enemy4,enemy4)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,3,enemy,enemy4,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,3,enemy,enemy2,enemy2) 
          else:
            print('Not an option')
            halt()      

        elif enemy.down == 0 and enemy2.down == 1 and enemy3.down == 0 and enemy4.down == 0:
          os.system('cls')
          print('Enemy 1  (1)          Enemy3  (3)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,3,enemy3,enemy4,enemy4)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,3,enemy,enemy4,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,3,enemy,enemy3,enemy3)

          else:
            print('Not an option')
            halt()      

        elif enemy.down == 1 and enemy2.down == 0 and enemy3.down == 0 and enemy4.down == 0:
          os.system('cls')
          print('Enemy 2  (2)          Enemy3  (3)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,3,enemy3,enemy4,enemy4)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,3,enemy2,enemy4,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,3,enemy2,enemy3,enemy3)

          else:
            print('Not an option')
            halt()      

        elif enemy.down == 1 and enemy2.down == 1 and enemy3.down == 0 and enemy4.down == 0: 
          os.system('cls')
          print('Enemy 3  (3)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,2,enemy4,enemy4,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,2,enemy3,enemy3,enemy3)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 1 and enemy2.down == 0 and enemy3.down == 1 and enemy4.down == 0: 
          os.system('cls')
          print('Enemy 2  (2)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,2,enemy4,enemy4,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,2,enemy2,enemy2,enemy2)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 1 and enemy2.down == 0 and enemy3.down == 0 and enemy4.down == 1: 
          os.system('cls')
          print('Enemy 2  (2)          Enemy3  (3)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,2,enemy3,enemy3,enemy3)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 0 and enemy2.down == 1 and enemy3.down == 1 and enemy4.down == 0: 
          os.system('cls')
          print('Enemy 1  (1)          Enemy4  (4)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,2,enemy4,enemy4,enemy4)
          elif com2 == '4':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy4,com,2,enemy,enemy,enemy)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 0 and enemy2.down == 1 and enemy3.down == 0 and enemy4.down == 1: 
          os.system('cls')
          print('Enemy 1  (1)          Enemy3  (3)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,2,enemy3,enemy3,enemy3)
          elif com2 == '3':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy3,com,2,enemy,enemy,enemy)
          else:
            print('Not an option')
            halt()

        elif enemy.down == 0 and enemy2.down == 0 and enemy3.down == 1 and enemy4.down == 1: 
          os.system('cls')
          print('Enemy 1  (1)          Enemy2  (2)')
          com2 = input('Which enemy is the target?  ')
          if com2 == '1':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy,com,2,enemy2,enemy2,enemy2)
          elif com2 == '2':
            os.system('cls')
            print(Fore.GREEN + 'Your spells are:\n')
            spells()
            com = input('\n\nWhich spell do you cast?  ')
            spellAttack(enemy2,com,2,enemy,enemy,enemy)
          else:
            print('Not an option')
            halt()

        elif enemy2.down == 1 and enemy3.down == 1 and enemy4.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy,com,1,enemy,enemy,enemy)

        elif enemy.down == 1 and enemy3.down == 1 and enemy4.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy2,com,1,enemy2,enemy2,enemy2)

        elif enemy.down == 1 and enemy2.down == 1 and enemy4.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy3,com,1,enemy3,enemy3,enemy3)

        elif enemy.down == 1 and enemy2.down == 1 and enemy3.down == 1:
          os.system('cls')
          print(Fore.GREEN + 'Your spells are:\n')
          spells()
          com = input('\n\nWhich spell do you cast?  ')
          spellAttack(enemy4,com,1,enemy4,enemy4,enemy4)
        i = 1
      elif com == 'e':
        playerHeal()
        i = 1
      elif com == '':
        i = 1
      else:
        print('not an option')
        halt()


    if enemy.H <= 0 and enemy.DTXT == False:
      os.system('cls')
      print('Enemy 1 dies!')
      halt()
      screen[enemy.ETile]['display'] = '  '
      enemy.down = 1
      enemy.DTXT = True

    if enemy2.H <= 0 and enemy2.DTXT == False:
      os.system('cls')
      print('Enemy 2 dies!')
      halt()
      screen[enemy2.ETile]['display'] = '  '
      enemy2.down = 1
      enemy2.DTXT = True

    if enemy3.H <= 0 and enemy3.DTXT == False:
      os.system('cls')
      print('Enemy 3 dies!')
      halt()
      screen[enemy3.ETile]['display'] = fg(236) + '@@'
      enemy3.down = 1
      enemy3.DTXT = True

    if enemy4.H <= 0 and enemy4.DTXT == False:
      os.system('cls')
      print('Enemy 4 dies!')
      halt()
      screen[enemy4.ETile]['display'] = fg(236) + '@@'
      enemy4.down = 1
      enemy4.DTXT = True

    if enemy.down == 1 and enemy2.down == 1 and enemy3.down == 1 and enemy4.down == 1:
      os.system('cls')
      print('The Enemies are defeated!')
      halt()
      x = 1



    os.system('cls')
    if enemy.down == 0:
      if enemy.WTimer == 0:
        s = enemy.ESpeed
        while s >= 1:
          if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
            s = 0
          else:
            screen[enemy.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy.ETile]['y'],screen[enemy.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy, 4, enemy2, enemy3, enemy4)
            screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 1 MOVMENT--')
            battlemap()
            halt()          
          s -= 1  
        screen[enemy.ETile]['display'] = Fore.RED + '@1' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 1 is stuck!')
        enemy.WTimer -= 1

      if Player.CTile == enemy.ETile + 20 or Player.CTile == enemy.ETile - 20 or Player.CTile == enemy.ETile + 1 or Player.CTile == enemy.ETile - 1 or Player.CTile == enemy.ETile +21 or Player.CTile == enemy.ETile -21 or Player.CTile == enemy.ETile +19 or Player.CTile == enemy.ETile -19:
        print(Fore.RED + '--ENEMY 1 TURN--')
        battlemap()        
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 1 misses!')
        else:
          print(Fore.RED + 'Enemy 1 hits for ' + str(enemy.damage))
          Player.H -= enemy.damage
        print(Fore.RESET)
        halt()
    if enemy2.down == 0:
      if enemy2.WTimer == 0:
        s = enemy2.ESpeed
        while s >= 1:
          if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
            s = 0
          else:
            screen[enemy2.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy2.ETile]['y'],screen[enemy2.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy2, 4, enemy, enemy3, enemy4)
            screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 2 MOVMENT--')
            battlemap()
            halt()          
          s -= 1  
        screen[enemy2.ETile]['display'] = Fore.RED + '@2' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 2 is stuck!')
        enemy2.WTimer -= 1

      if Player.CTile == enemy2.ETile + 20 or Player.CTile == enemy2.ETile - 20 or Player.CTile == enemy2.ETile + 1 or Player.CTile == enemy2.ETile - 1 or Player.CTile == enemy2.ETile +21 or Player.CTile == enemy2.ETile -21 or Player.CTile == enemy2.ETile +19 or Player.CTile == enemy2.ETile -19:
        print(Fore.RED + '--ENEMY 2 TURN--')
        battlemap()        
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 2 misses!')
        else:
          print(Fore.RED + 'Enemy 2 hits for ' + str(enemy2.damage))
          Player.H -= enemy2.damage
        print(Fore.RESET)
        halt()
    if enemy3.down == 0:
      if enemy3.WTimer == 0:
        s = enemy3.ESpeed
        while s >= 1:
          if Player.CTile == enemy3.ETile + 20 or Player.CTile == enemy3.ETile - 20 or Player.CTile == enemy3.ETile + 1 or Player.CTile == enemy3.ETile - 1 or Player.CTile == enemy3.ETile +21 or Player.CTile == enemy3.ETile -21 or Player.CTile == enemy3.ETile +19 or Player.CTile == enemy3.ETile -19:
            s = 0
          else:
            screen[enemy3.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy3.ETile]['y'],screen[enemy3.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy3, 4, enemy, enemy2, enemy4)
            screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 3 MOVMENT--')
            battlemap()
            halt()          
          s -= 1  
        screen[enemy3.ETile]['display'] = Fore.RED + '@3' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 3 is stuck!')
        enemy3.WTimer -= 1

      if Player.CTile == enemy3.ETile + 20 or Player.CTile == enemy3.ETile - 20 or Player.CTile == enemy3.ETile + 1 or Player.CTile == enemy3.ETile - 1 or Player.CTile == enemy3.ETile +21 or Player.CTile == enemy3.ETile -21 or Player.CTile == enemy3.ETile +19 or Player.CTile == enemy3.ETile -19:
        print(Fore.RED + '--ENEMY 3 TURN--')
        battlemap()        
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 3 misses!')
        else:
          print(Fore.RED + 'Enemy 3 hits for ' + str(enemy3.damage))
          Player.H -= enemy3.damage
        print(Fore.RESET)
        halt()
    if enemy4.down == 0:
      if enemy4.WTimer == 0:
        s = enemy4.ESpeed
        while s >= 1:
          if Player.CTile == enemy4.ETile + 20 or Player.CTile == enemy4.ETile - 20 or Player.CTile == enemy4.ETile + 1 or Player.CTile == enemy4.ETile - 1 or Player.CTile == enemy4.ETile +21 or Player.CTile == enemy4.ETile -21 or Player.CTile == enemy4.ETile +19 or Player.CTile == enemy4.ETile -19:
            s = 0
          else:
            screen[enemy4.ETile]['display'] = '  '
            astar(rooms[Player.CRoom]['bmap'],(screen[enemy4.ETile]['y'],screen[enemy4.ETile]['x']),(screen[Player.CTile]['y'],screen[Player.CTile]['x']), enemy4, 4, enemy, enemy2, enemy3)
            screen[enemy4.ETile]['display'] = Fore.RED + '@4' + Fore.RESET
            os.system('cls')
            print(Fore.RED + '--ENEMY 4 MOVMENT--')
            battlemap()
            halt()          
          s -= 1  
        screen[enemy4.ETile]['display'] = Fore.RED + '@4' + Fore.RESET
        os.system('cls')
      else:
        print(Fore.WHITE + 'Enemy 4 is stuck!')
        enemy4.WTimer -= 1

      if Player.CTile == enemy4.ETile + 20 or Player.CTile == enemy4.ETile - 20 or Player.CTile == enemy4.ETile + 1 or Player.CTile == enemy4.ETile - 1 or Player.CTile == enemy4.ETile +21 or Player.CTile == enemy4.ETile -21 or Player.CTile == enemy4.ETile +19 or Player.CTile == enemy4.ETile -19:
        print(Fore.RED + '--ENEMY 4 TURN--')
        battlemap()        
        hit = random.randint(1,100)
        hit -= items[Player.armour]['def']
        if hit < 1:
          print(Fore.GREEN + 'Enemy 4 misses!')
        else:
          print(Fore.RED + 'Enemy 4 hits for ' + str(enemy4.damage))
          Player.H -= enemy4.damage
        print(Fore.RESET)
        halt()




    os.system('cls')
    if Player.H <= 0:
      os.system('cls')
      print('You Died!')
      halt()
      x = 1




def resetcolours():
  for n in rooms:
    if n == r8 or n == r32 or n == r45 or n == r53 or n == r62 or n == r67 or n == r79 or n == r89 or n == r93 or n == r94 or n == r105 or n == r116 or n == r125 or n == r131 or n == r143 or n == r157 or n == r167:
      if rooms[n]['seen'] == 1:
        rooms[n]['mmc'] = Fore.YELLOW    
      else:
        rooms[n]['mmc'] = fg(0)
    else:
      if rooms[n]['seen'] == 1:
        rooms[n]['mmc'] = Fore.RESET     
      else:
        rooms[n]['mmc'] = fg(0)



def enc1(enemy):
  x = 0
  while x == 0:
    print('You encountered '+Fore.RED + enemy.name)
    com = input('What action:'+Fore.BLUE+' \nRun (r)\n'+Fore.RED+'Fight  (f)'+Fore.RESET+'\n\n')

    if com == 'Run' or com == 'r':
      r = random.randint(1,6)
      if r != 6:
        Player.CRoom = Player.PreRoom
        print('Ran successfuly')
        halt()
        os.system('cls')
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
    if enemy.down == 1:
      Player.xp  += enemy.XP
      print('Gained ' + str(enemy.XP) + 'XP points!')


def enc2(enemy,enemy2):
  x = 0
  while x == 0:
    print('You encountered '+Fore.RED + enemy.name + ' and ' + enemy2.name)
    com = input('What action:'+Fore.BLUE+' \nRun (r)\n'+Fore.RED+'Fight  (f)'+Fore.RESET+'\n\n')

    if com == 'Run' or com == 'r':
      r = random.randint(1,6)
      if r != 6:
        Player.CRoom = Player.PreRoom
        print('Ran successfuly')
        halt()
        os.system('cls')
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
  if enemy.down == 1 and enemy2.down == 1:
    Player.xp  += enemy.XP
    print('Gained ' + str(enemy.XP) + 'XP points!')


def enc3(enemy,enemy2,enemy3):
  x = 0
  while x == 0:
    print('You encountered '+Fore.RED + enemy.name + '  ,  ' + enemy2.name + '  and  ' + enemy3.name)
    com = input('What action:'+Fore.BLUE+' \nRun (r)\n'+Fore.RED+'Fight  (f)'+Fore.RESET+'\n\n')

    if com == 'Run' or com == 'r':
      r = random.randint(1,6)
      if r != 6:
        Player.CRoom = Player.PreRoom
        print('Ran successfuly')
        halt()
        os.system('cls')
        x = 1
      else:
        print('Failed, combat is engaged')
        halt()
        os.system('cls')
        fight3(enemy, enemy2, enemy3)
        x = 1
    elif com == 'Fight' or com == 'f':
      os.system('cls')
      fight3(enemy, enemy2, enemy3)
      x = 1
    else:
     print('not an option')
     os.system('cls')
  if enemy.down == 1 and enemy2.down == 1 and enemy3.down == 1:
    Player.xp  += enemy.XP
    print('Gained ' + str(enemy.XP) + 'XP points!')


def enc4(enemy,enemy2,enemy3,enemy4):
  x = 0
  while x == 0:
    print('You encountered '+Fore.RED + enemy.name + ',  ' + enemy2.name + ',  ' + enemy3.name + '   and  ' + enemy4.name)
    com = input('What action:'+Fore.BLUE+' \nRun (r)\n'+Fore.RED+'Fight  (f)'+Fore.RESET+'\n\n')

    if com == 'Run' or com == 'r':
      r = random.randint(1,6)
      if r != 6:
        Player.CRoom = Player.PreRoom
        print('Ran successfuly')
        halt()
        os.system('cls')
        x = 1
      else:
        print('Failed, combat is engaged')
        halt()
        os.system('cls')
        fight4(enemy, enemy2, enemy3, enemy4)
        x = 1
    elif com == 'Fight' or com == 'f':
      os.system('cls')
      fight4(enemy, enemy2, enemy3, enemy4)
      x = 1
    else:
     print('not an option')
     os.system('cls')
  if enemy.down == 1 and enemy2.down == 1 and enemy3.down == 1 and enemy4.down == 1:
    Player.xp  += enemy.XP
    print('Gained ' + str(enemy.XP) + 'XP points!')




print(Fore.BLUE)
os.system('cls')
print('--<IMPORTANT>--\n\n'+fg(190)+'Make sure to read what actions you can take at any given spot\nSpecial actions appear in different colours, such as\n'+Fore.RED+'search (q)\n'+Fore.YELLOW+'rest (r)\n'+Fore.BLUE+'Map (m)\n'+fg(190)+'Inputs you can make are always put with brackets around them, such as menu selection.')
halt()
print(Fore.RESET)
os.system('cls')
stop = 0
y=0
while y == 0:
  if Player.H <= 0:
    p = 0
    while p == 0:
      c = input('Continue from last rest point?    y/n\n\n')
      if c == 'n' or c == 'N':
        stop = 1
        p = 1
      elif c == 'y' or c == 'Y':
        os.system('cls')
        stop = 0
        p = 1
        Player.CRoom = Player.lastRest
        Player.H = Player.maxH
        Player.SP = Player.spellSL

      else:
        print('not an option')
        os.system('cls')
  if stop == 1:
    break
  resetcolours()
  rooms[Player.CRoom]['mmc'] = Fore.GREEN
  if Enemy0A.down == 0 and rooms[Enemy0A.ERoom]['seen'] == 1 or Enemy0B.down == 0 and rooms[Enemy0A.ERoom]['seen'] == 1:
    rooms[Enemy0A.ERoom]['mmc'] = Fore.RED
  if Enemy1.down == 0 and rooms[Enemy1.ERoom]['seen'] == 1:
    rooms[Enemy1.ERoom]['mmc'] = Fore.RED
  if Enemy2A.down == 0 and rooms[Enemy2A.ERoom]['seen'] == 1 or Enemy2B.down == 0 and rooms[Enemy2A.ERoom]['seen'] == 1:
    rooms[Enemy2A.ERoom]['mmc'] = Fore.RED
  if Enemy3A.down == 0 and rooms[Enemy3A.ERoom]['seen'] == 1  or Enemy3B.down == 0 and rooms[Enemy3A.ERoom]['seen'] == 1:
    rooms[Enemy3A.ERoom]['mmc'] = Fore.RED
  if Enemy4.down == 0 and rooms[Enemy4.ERoom]['seen'] == 1:
    rooms[Enemy4.ERoom]['mmc'] = Fore.RED
  if Enemy5.down == 0 and rooms[Enemy5.ERoom]['seen'] == 1:
    rooms[Enemy5.ERoom]['mmc'] = Fore.RED
  if Enemy6.down == 0 and rooms[Enemy6.ERoom]['seen'] == 1:
    rooms[Enemy6.ERoom]['mmc'] = Fore.RED
  if Enemy7.down == 0 and rooms[Enemy7.ERoom]['seen'] == 1:
    rooms[Enemy7.ERoom]['mmc'] = Fore.RED
  if Enemy8.down == 0 and rooms[Enemy8.ERoom]['seen'] == 1:
    rooms[Enemy8.ERoom]['mmc'] = Fore.RED
  if Sen1A.down == 0 and rooms[Sen1A.ERoom]['seen'] == 1 or Sen1B.down == 0 and rooms[Sen1A.ERoom]['seen'] == 1  or Sen1C.down == 0 and rooms[Sen1A.ERoom]['seen'] == 1  or Sen1D.down == 0 and rooms[Sen1A.ERoom]['seen'] == 1 :
    rooms[Sen1A.ERoom]['mmc'] = Fore.RED
  if Sen2A.down == 0 and rooms[Sen2A.ERoom]['seen'] == 1  or Sen2B.down == 0 and rooms[Sen2A.ERoom]['seen'] == 1  or Sen2C.down == 0 and rooms[Sen2A.ERoom]['seen'] == 1 :
    rooms[Sen2A.ERoom]['mmc'] = Fore.RED
  if Enemy9A.down == 0 and rooms[Enemy9A.ERoom]['seen'] == 1 or Enemy9B.down == 0 and rooms[Enemy9A.ERoom]['seen'] == 1:
    rooms[Enemy9A.ERoom]['mmc'] = Fore.RED
  if Enemy10.down == 0 and rooms[Enemy10.ERoom]['seen'] == 1:
    rooms[Enemy10.ERoom]['mmc'] = Fore.RED
  if Enemy11.down == 0 and rooms[Enemy11.ERoom]['seen'] == 1:
    rooms[Enemy11.ERoom]['mmc'] = Fore.RED
  if Enemy12A.down == 0 and rooms[Enemy12A.ERoom]['seen'] == 1  or Enemy12B.down == 0 and rooms[Enemy12A.ERoom]['seen'] == 1  or Enemy12C.down == 0 and rooms[Enemy12A.ERoom]['seen'] == 1 :
    rooms[Enemy12A.ERoom]['mmc'] = Fore.RED
  if Enemy13A.down == 0 and rooms[Enemy13A.ERoom]['seen'] == 1 or Enemy13B.down == 0 and rooms[Enemy13A.ERoom]['seen'] == 1:
    rooms[Enemy13A.ERoom]['mmc'] = Fore.RED
  if Enemy14.down == 0 and rooms[Enemy14.ERoom]['seen'] == 1:
    rooms[Enemy14.ERoom]['mmc'] = Fore.RED
  if Enemy15.down == 0 and rooms[Enemy15.ERoom]['seen'] == 1:
    rooms[Enemy15.ERoom]['mmc'] = Fore.RED
  if Enemy16A.down == 0 and rooms[Enemy16A.ERoom]['seen'] == 1  or Enemy16B.down == 0 and rooms[Enemy16A.ERoom]['seen'] == 1  or Enemy16C.down == 0 and rooms[Enemy16A.ERoom]['seen'] == 1 :
    rooms[Enemy16A.ERoom]['mmc'] = Fore.RED
  if Enemy17A.down == 0 and rooms[Enemy17A.ERoom]['seen'] == 1 or Enemy17B.down == 0 and rooms[Enemy17A.ERoom]['seen'] == 1:
    rooms[Enemy17A.ERoom]['mmc'] = Fore.RED
  if Sen3A.down == 0 and rooms[Sen3A.ERoom]['seen'] == 1 or Sen3B.down == 0 and rooms[Sen3A.ERoom]['seen'] == 1  or Sen3C.down == 0 and rooms[Sen3A.ERoom]['seen'] == 1  or Sen3D.down == 0 and rooms[Sen3A.ERoom]['seen'] == 1 :
    rooms[Sen3A.ERoom]['mmc'] = Fore.RED
  if Enemy18A.down == 0 and rooms[Enemy18A.ERoom]['seen'] == 1  or Enemy18B.down == 0 and rooms[Enemy18A.ERoom]['seen'] == 1  or Enemy18C.down == 0 and rooms[Enemy18A.ERoom]['seen'] == 1 :
    rooms[Enemy18A.ERoom]['mmc'] = Fore.RED
  if Enemy19.down == 0 and rooms[Enemy19.ERoom]['seen'] == 1:
    rooms[Enemy19.ERoom]['mmc'] = Fore.RED
  if Enemy20.down == 0 and rooms[Enemy20.ERoom]['seen'] == 1:
    rooms[Enemy20.ERoom]['mmc'] = Fore.RED
  if Enemy21A.down == 0 and rooms[Enemy21A.ERoom]['seen'] == 1 or Enemy21B.down == 0 and rooms[Enemy21A.ERoom]['seen'] == 1  or Enemy21C.down == 0 and rooms[Enemy21A.ERoom]['seen'] == 1  or Enemy21D.down == 0 and rooms[Enemy21A.ERoom]['seen'] == 1 :
    rooms[Enemy21A.ERoom]['mmc'] = Fore.RED
  if Enemy22A.down == 0 and rooms[Enemy22A.ERoom]['seen'] == 1  or Enemy22B.down == 0 and rooms[Enemy22A.ERoom]['seen'] == 1  or Enemy22C.down == 0 and rooms[Enemy22A.ERoom]['seen'] == 1 :
    rooms[Enemy22A.ERoom]['mmc'] = Fore.RED
  if Sen4A.down == 0 and rooms[Sen4A.ERoom]['seen'] == 1 or Sen4B.down == 0 and rooms[Sen4A.ERoom]['seen'] == 1  or Sen4C.down == 0 and rooms[Sen4A.ERoom]['seen'] == 1  or Sen4D.down == 0 and rooms[Sen4A.ERoom]['seen'] == 1 :
    rooms[Sen4A.ERoom]['mmc'] = Fore.RED



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
  elif rooms[Player.CRoom]['minimap'] == 'lakes':
    lakes()
  elif rooms[Player.CRoom]['minimap'] == 'ship':
    ship()
  elif rooms[Player.CRoom]['minimap'] == 'hold':
    hold()
  elif rooms[Player.CRoom]['minimap'] == 'haunt':
    haunt()
  elif rooms[Player.CRoom]['minimap'] == 'wisp':
    wisp()
  elif rooms[Player.CRoom]['minimap'] == 'dark':
    dark()





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
        if com2 == '14':
          com2 = 'Ocean Reaver'
        if com2 == '15':
          com2 = 'Blunderbuss'
        if com2 == '16':
          com2 = 'Scale Mail'


        if com2 in items:
          if items[com2]['num'] != 0:
            if items[com2]['equ'] == 'wea':
              if Player.weapon == 'Staff of the Magi':
                Player.spellSL = Player.normSP
                Player.SP -= 2
                if Player.SP < 0:
                  Player.SP = 0
              items[Player.weapon]['wEquiped'] = 'no'
              items[com2]['wEquiped'] = 'yes'
              Player.weapon = com2
              if Player.weapon == 'Staff of the Magi':
                Player.spellSL = Player.normSP + 2
                Player.SP += 2
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
        if com2 == '11':
          com2 = 'Smite (Scroll)'
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
              os.system('cls')
              print(spList)
              if len(spList) == 1:
                print('   (1)')
              if len(spList) == 2:
                print('   (1)                      (2)')
              if len(spList) == 3:
                print('   (1)                      (2)                      (3)')
              if len(spList) == 4:
                print('   (1)                      (2)                      (3)                      (4)')
              if len(spList) == 5:
                print('   (1)                      (2)                      (3)                      (4)                      (5)')

              com3 = input('\nSpell list full, which item do you want to remove?   ')
              if com3 == '1':
                com3 = spList[0]
              elif com3 == '2' and len(spList) >= 2:
                com3 = spList[1]
              elif com3 == '3' and len(spList) >= 3:
                com3 = spList[2]
              elif com3 == '4' and len(spList) >= 4:
                com3 = spList[3]
              elif com3 == '5' and len(spList) >= 5:
                com3 = spList[4]

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
      else:
        print('not an option')  
        halt()
        x = 1

    elif com == 'r' and rooms[Player.CRoom]['rest'] == 'y':
      rooms[Player.CRoom]['rest'] = 'n'
      print('Health and SP restored, Rest point stored as restart point')
      Player.SP = Player.spellSL
      Player.H = Player.maxH
      Player.lastRest = Player.CRoom
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




  if Player.CRoom == Enemy0A.ERoom and Enemy0A.down == 0 or  Player.CRoom == Enemy0A.ERoom and Enemy0B.down == 0:
    enc2(Enemy0A,Enemy0B)

  if Player.CRoom == Enemy1.ERoom and Enemy1.down == 0:
    enc1(Enemy1)  

  if Player.CRoom == Enemy2A.ERoom and Enemy2A.down == 0 or Player.CRoom == Enemy2A.ERoom and Enemy2B.down == 0:
    enc2(Enemy2A,Enemy2B)  

  if Player.CRoom == Enemy3A.ERoom and Enemy3A.down == 0 and Player.CRoom == Enemy3A.ERoom and Enemy3B.down == 0:
    enc2(Enemy3A,Enemy3B)  

  if Player.CRoom == Enemy4.ERoom and Enemy4.down == 0:
    enc1(Enemy4)  

  if Player.CRoom == Enemy5.ERoom and Enemy5.down == 0:
    enc1(Enemy5)  

  if Player.CRoom == Enemy6.ERoom and Enemy6.down == 0:
    enc1(Enemy6)  

  if Player.CRoom == Enemy7.ERoom and Enemy7.down == 0:
    enc1(Enemy7)  

  if Player.CRoom == Enemy8.ERoom and Enemy8.down == 0:
    enc1(Enemy8)  

  if Player.CRoom == Sen1A.ERoom and Sen1A.down == 0 or Player.CRoom == Sen1B.ERoom and Sen1B.down == 0 or Player.CRoom == Sen1C.ERoom and Sen1C.down == 0 or Player.CRoom == Sen1D.ERoom and Sen1D.down == 0:
    enc4(Sen1A,Sen1B,Sen1C,Sen1D) 

  if Player.CRoom == Sen2A.ERoom and Sen2A.down == 0 or Player.CRoom == Sen2A.ERoom and Sen2B.down == 0 or Player.CRoom == Sen2A.ERoom and Sen2C.down == 0:
    enc3(Sen2A,Sen2B,Sen2C) 

  if Player.CRoom == Enemy9A.ERoom and Enemy9A.down == 0 or  Player.CRoom == Enemy9A.ERoom and Enemy9B.down == 0:
    enc2(Enemy9A,Enemy9B)

  if Player.CRoom == Enemy10.ERoom and Enemy10.down == 0:
    enc1(Enemy10) 

  if Player.CRoom == Enemy11.ERoom and Enemy11.down == 0:
    enc1(Enemy11) 

  if Player.CRoom == Enemy12A.ERoom and Enemy12A.down == 0 or Player.CRoom == Enemy12A.ERoom and Enemy12B.down == 0 or Player.CRoom == Enemy12A.ERoom and Enemy12C.down == 0:
    enc3(Enemy12A,Enemy12B,Enemy12C) 

  if Player.CRoom == Enemy13A.ERoom and Enemy13A.down == 0 or  Player.CRoom == Enemy13A.ERoom and Enemy13B.down == 0:
    enc2(Enemy13A,Enemy13B)

  if Player.CRoom == Enemy14.ERoom and Enemy14.down == 0:
    enc1(Enemy14) 

  if Player.CRoom == Enemy15.ERoom and Enemy15.down == 0:
    enc1(Enemy15) 

  if Player.CRoom == Enemy16A.ERoom and Enemy16A.down == 0 or Player.CRoom == Enemy16A.ERoom and Enemy16B.down == 0 or Player.CRoom == Enemy16A.ERoom and Enemy16C.down == 0:
    enc3(Enemy16A,Enemy16B,Enemy16C) 

  if Player.CRoom == Enemy17A.ERoom and Enemy17A.down == 0 or  Player.CRoom == Enemy17A.ERoom and Enemy17B.down == 0:
    enc2(Enemy17A,Enemy17B)

  if Player.CRoom == Sen3A.ERoom and Sen3A.down == 0 or Player.CRoom == Sen3B.ERoom and Sen3B.down == 0 or Player.CRoom == Sen3C.ERoom and Sen3C.down == 0 or Player.CRoom == Sen3D.ERoom and Sen3D.down == 0:
    enc4(Sen3A,Sen3B,Sen3C,Sen3D) 

  if Player.CRoom == Enemy18A.ERoom and Enemy18A.down == 0 or Player.CRoom == Enemy18A.ERoom and Enemy18B.down == 0 or Player.CRoom == Enemy18A.ERoom and Enemy18C.down == 0:
    enc3(Enemy18A,Enemy18B,Enemy18C) 

  if Player.CRoom == Enemy19.ERoom and Enemy19.down == 0:
    enc1(Enemy19) 

  if Player.CRoom == Enemy20.ERoom and Enemy20.down == 0:
    enc1(Enemy20) 

  if Player.CRoom == Enemy21A.ERoom and Enemy21A.down == 0 or Player.CRoom == Enemy21B.ERoom and Enemy21B.down == 0 or Player.CRoom == Enemy21C.ERoom and Enemy21C.down == 0 or Player.CRoom == Enemy21D.ERoom and Enemy21D.down == 0:
    enc4(Enemy21A,Enemy21B,Enemy21C,Enemy21D)     

  if Player.CRoom == Enemy22A.ERoom and Enemy22A.down == 0 or Player.CRoom == Enemy22A.ERoom and Enemy22B.down == 0 or Player.CRoom == Enemy22A.ERoom and Enemy22C.down == 0:
    enc3(Enemy22A,Enemy22B,Enemy22C) 

  if Player.CRoom == Sen4A.ERoom and Sen4A.down == 0 or Player.CRoom == Sen4B.ERoom and Sen4B.down == 0 or Player.CRoom == Sen4C.ERoom and Sen4C.down == 0 or Player.CRoom == Sen4D.ERoom and Sen4D.down == 0:
    enc4(Sen4A,Sen4B,Sen4C,Sen4D) 



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
    Player.normSP += 1
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
  if Player.xp >= 500 and Player.level < 6:
    print('You leveled up to LVL 6!\nHP increases by 20')
    Player.level = 6
    Player.maxH += 20
    Player.H += 20
  if Player.xp >= 670 and Player.level < 7:
    print('You leveled up to LVL 7!\nHP increases by 20   and   Gain 1 Max SP')
    Player.level = 7
    Player.maxH += 20
    Player.H += 20
    Player.spellSL += 1
    Player.SP += 1    
    Player.normSP += 1
  if Player.xp >= 840 and Player.level < 8:
    print('You leveled up to LVL 8!\nHP increases by 20')
    Player.level = 8
    Player.maxH += 20
    Player.H += 20
  if Player.xp >= 940 and Player.level < 9:
    print('You leveled up to LVL 9!\nHP increases by 20   and   Gain 1 Base Speed')
    Player.level = 9
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
