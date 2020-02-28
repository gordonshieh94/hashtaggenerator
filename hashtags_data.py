#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Map string identifier to list
LIST_MAP = {}

GENERIC = 'generic'
generic = [
    "#broadmag",
    "#exploreobserveshare",
    "#magazine35mm",
    "#lookslikefilm",
    "#cerealmag",
    "#weltraumzine",
    "#oldtonecollective",
    "#exploreobserveshare",
    "#weltraumzine",
    "#imaginarymagnitude",
    "#somewheremagazine",
    "#ignant",
    "#stademagazine",
    "#satellitetales",
]
LIST_MAP[GENERIC] = generic

FUJIFLM = 'fujifilm'
fujifilm = [
  "#fujilove",
  "#fujifeed",
  "#fujifilm_global",
]
LIST_MAP[FUJIFLM] = fujifilm

# 100k+ followers
PORTRAIT_L = 'portrait_l'
portrait_l = [
    "@quietthechaos #quietthechaos",
    "@portraitpage #portraitpage",
    "@waitingontheworld #ftwotw",
    "@ofhumans #featuredmeofh",
    "@expofilm #expofilm",
    "@dark.daisies #ftmedd",
    "@l0tsabraids_ #l0tsabraids",
    "@hinfluencercollective #hinfluencercollective",
    "@sticks_and_stones_agency #postmypicssticks",
    "@cheadsmagazine #cheadsmagazine",
    "@marvelous_shots #marvelous_shots",
    "@myphotoshop_ #myphotoshop",
    "@of2humans #of2humans",
    "@earth_portraits #earth_portraits",
    "@aovportraits #aovportraits",
    "@theportraitpr0ject #theportraitpr0ject",
    "@portraitmood #portraitmood",
    "@darkmornings #darkmornings",
    "@filmpalette #featurepalette",
    "@portraitmood",
    "@silver.seas #featuremeseas",
    "@igpodium_portraits #igpodium_portraits",
    "@freepeople -#freepeople",
    "@hot_is_the_new_black #hotisthenewblack",
    "@createcommune #createcommune",
    "@portraitsfromtheworld #portraitsfromtheworld",
    "@kdpeoplegallery  #kdpeoplegallery",
    "@majestic_people_ #majestic_people_",
    "@portraits_mf #portraits_mf",
    "@portraitfestival #portraitfestival",
    "@peoplephotatoes #peoplephotatoes",
    "@portraitsfromtheworld #portraitsfromtheworld",
    "@ourmoodydays #ourmoodydays",
    "@endlessfaces #endlessfaces",
    "@bravogreatphoto #bravogreatphoto",
    "@last.daze #lastdaze",
    "@thoughtcatalog #thoughtcatalog 172k followers",
]
LIST_MAP[PORTRAIT_L] = portrait_l

# 50k-100k followers
PORTRAIT_M = 'portrait_m'
portrait_m = [
    "@tangledinfilm #tangledinfilm",
    "@pursuitofportraits #pursuitofportraits",
    "@oblivioncreature #featureacreature",
    "@winterwillneverend #ftwwne",
    "@portraitvision #portraitvision",
    "@postthepeople #postthepeople",
    "@peoplefeature #featuremepf",
    "@makeportrait #makeportraits",
    "@instagramskilla #gramkilla",
    "@oceanfeatures #cooloceann",
    "@globe_people #globe_people",
    "@2instagood #2instagoodportraitlove",
    "@seekingthestars #seekingthestars",
    "@portraits_mf #portraits_mf",
    "@moodyports #moodyports",
    "@pr0ject_soul #pr0ject_soul",
    "@bravoportraits #bravoportraits",
    "@rainbow.features #rainbowfeatures",
    "@vscoportrait #vcsoportrait",
    "@folkportraits #folkportraits",
    "@makeportrait #makeportrait",
    "@vscoportrait #vscoportrait",
]
LIST_MAP[PORTRAIT_M] = portrait_m

# 20k-50k followers
PORTRAIT_S = 'portrait_small'
portrait_s = [
    "@vogove #vogove",
    "@portrait_society #portraitsociety",
    "@luisthechickengod #theswaggingchicken",
    "@herefallsthenight #herefallsthenight",
    "@discoverportrait #discoverportrait",
    "@makeportraitsmag #makeportraitsmag",
    "@earth.portraits #earthportraits",
    "@portraitgames #portraitgames",
    "@portrait_perfection #portraitperfection",
    "@portraitfolk #portraitfolk",
    "@creative_portraits #creative_portraits",
    "@hvmansouls #hvmansouls",
    "@lensofourlives #lensofourlives",
    "@portraitstream #portraitstream",
    "@portraitsmag #portraitsmag",
    "@yourvisiongallery #yourvisiongallery",
    "@projectphotoshop #projectphotoshop",
]
LIST_MAP[PORTRAIT_S] = portrait_s

# less than 20k followers
PORTRAIT_XS = 'portrait_xsmall'
portrait_xs = [
    "less than 20k followers",
    "@portraitsofgirls #portraitsofgirls",
    "@portrait_vision #portrait_vision",
    "@portraitfeature #portraitfeature",
    "@artofportrait_ #artofportrait",
    "@777luckyfish #777luckyfish",
    "@pulsefilm #pulsefilm",
    "@ig_muse #ig_muse",
    "@skilled_portraits #skilled_portraits",
    "@iiwiimag #iiwiimag",
    "@watchingfilms #featuremefilms",
    "@envisiontones #envisiontones",
    "@oursecrethidden #oursecrethidden",
    "@modernmoons #modernmoons",
    "@chasingessence #chasingessence",
    "@featureacc #featureworlds",
    "@flakemagazine #featuremeflake",
    "@obliviousfilm #featuremeof",
    "@creative_portraits #creative_portraits",
    "@portraitsatl #portraitsatl",
    "@portraits_la #portraitsla",
    "@portraitkillers #portraitkillers",
    "@ambientfeature #ambientfeature",
    "@artistfound #artistfound",
    "@exploremoreportraits #exploremore",
    "#shootlikeaboss",
    "#xelfies",
    "#portraitmeet",
    "#awesomeportrait",
    "#hurtlamb",
    "#theportraitcentral",
]
LIST_MAP[PORTRAIT_XS] = portrait_xs

YAYAREA = 'yayarea'
yayarea = [
    "#bayareaphotographer",
    "#bayareaphotography",
    "#bayareamodel",
    "#bayareamodels",
    "#sacramentophotographer",
    "#sacramentophotography",
    "#sacmodel",
    "#sacramentomodel",
    "#norcalphotographer",
    "#norcalphotography",
    "#californiaphotographer",
    "#californiaphotography",
    "#sanjosephotographer",
    "#sanjosephotography",
    "#sfphotographer",
    "#sfphotography",
    "#sfmodel",
    "#westcoastusa"
]
LIST_MAP[YAYAREA] = yayarea

POPULAR_PORTRAIT = 'popular_portrait'
popular_portrait = [
  "#portraitphotography",
  "#artofvisuals",
  "#777luckyfish",
  "#portvisual",
  "#pursuitofportrait",
  "#theportraitpro0ject",
  "#portraitvisuals",
  "#weshoothumans",
  "#portraitsociety",
  "#portrait_mood",
  "#portrait_star",
  "#portrait_vision",
  "#portraitvision",
  "#portrait_mf",
  "#discoverportraits",
  "#portraitstream",
  "#portraitgasm",
  "#portraitsquad",
  "#portraitkillers",
  "#portrait_wizard",
  "#under10kportraits",
  "#wmportraits",
  "#portraitfeed",
  "#portraituniverse",
  "#nextvisualportraits",
  "#aovportraits",
  "#ourportraitdays",
  "#bravogreatportrait",
  "#portraitsinspire",
  "#portraitspg",
  "#justportrait",
  "#bestshooter_portraits",
  "#portrait_shots",
  "#portrait_today",
  "#portraitlovers",
  "#portraitureinspirations",
  "#germanportraiture",
  "#portraitshooting",
  "#ig_ports",
  "#top_portraits",
  "#portraitstyles_gf",
  "#life_portraits",
  "#rsa_portraits",
  "#portraits_universe",
  "#majestic_people",
  "#portraitpage",
  "#igpodium_portraits",
  "#portraitmood",
  "#portraiture",
  "#portraits",
  "#portraitphotographer",
  "#agameofportraits",
  "#moodyports",
  "#portraidhood",
  "#portraitcentral",
  "#theportraitcentral",
  "#portraitsmag",
  "#worldofportraits",
  "#folkportrait",
  "#globe_people",
  "#portraits_perfection",
  "#portrait_shooterz",
  "#portrait_shooters",
  "#portrait_pros",
  "#portrait_styles",
  "#thelightsofbeauty",
  "#doports",
  "#portraisedition",
  "#yourvisiongallery",
  "#theportraitculture",
  "#portraitgames",
  "#gramkilla",
  "#igportrait",
  "#portrait_shot",
  "#creativeportraits",
  "#portraitfestival",
  "#portraits_today",
  "#endlessfaces",
  "#ig_muse",
  "#artofportrait",
  "#portrait_legit",
  "#portraitinspiration"
  "#discoverunder1k",
  "#discoverunder20k",
  "#discoverunder10k",
  "#portraitlove",
  "#instagood",
  "#theworldofportraits",
  "#portraitscam",
  "#portraitplay",
  "#creatives_lounge",
  "#quietthechaos",
  "#ftwotw",
  "#ftmedd",
  "#l0tsabraids",
  "#hinfluencercollective",
  "#postmypicssticks",
  "#cheadsmagazine",
  "#myphotoshop",
  "#of2humans",
  "#earthportraits",
  "#darkmornings",
  "#featurepalette",
  "#featuremeseas",
  "#freepeople",
  "#hotisthenewblack",
  "#createcommune",
  "#portraitsfromtheworld",
  "#kdpeoplegallery",
  "#peoplephotatoes",
  "#ourmoodydays",
  "#lastdaze",
  "#thoughtcatalog",
  "#featurecreature",
  "#ftwwne",
  "#postthepeople",
  "#featuremepf",
  "#makeportraits",
  "#cooloceann",
  "#2instagoodportraitlove",
  "#seekingthestars",
  "#pr0ject_soul",
  "#rainbowfeatures",
  "#vscoportrait",
  "#vogove",
  "#theswaggingchicken",
  "#portraitperfection",
  "#hvmansouls",
  "#lensofourlives",
  "#skilled_portraits",
  "#iiwiimang",
  "#envisiontones",
  "#oursecrethidden",
  "#modernmoons",
  "#chasingessence",
  "#featureworlds",
  "#featuremeflake",
  "#featuremeof",
  "#ambiantfeature",
  "#artistfound",
  "#exploremore",
  "#majesticcasual",
  "#24hrchruch"
  "#thecreatorclass"
]
LIST_MAP[POPULAR_PORTRAIT] = popular_portrait

FINE_ART = 'fine_art'
fine_art = [
    "#fineart",
    "#hurtlamb",
    "#ifyouleave",
    "subjectivelyobjective",
    "indies_minimal",
    "#staybasicly",
]
LIST_MAP[FINE_ART] = fine_art

STREET = 'street'
street = [
    "#streetphotography",
    "#lensonstreets",
    "#thesmartview",

]
LIST_MAP[STREET] = street

MINIMALISM = 'minimalism'
minimalism = [
    "#gominimalmag",
    "#lucecurated",
]
LIST_MAP[MINIMALISM] = minimalism

BNW = 'bnw'
bnw = [
    "#lightandshadow",
]
LIST_MAP[BNW] = bnw

FILM = 'film'
film =[
    "#filmphotographers",
    "#filmphotographyday",
    "#filmphotoshare",
    "#filmphotografic",
    "#filmphotographyisnotdead",
    "#filmphotographybaguio",
    "#filmphotorussia",
    "#filmphotographyisgrowing",
    "#filmphotographyindia",
    "#filmphotogram",
    "#filmphoto",
    "#filmphotographic",
    "#filmphotographer",
    "#filmphotograph",
    "#filmphotos",
    "#filmphotooftheday",
    "#filmphotographyproject",
    "#analog",
    "#analogue",
    "#analogfilm",
    "#analogphotography",
    "#analoguevibes",
    "#analogblog",
    "#analogpeople",
    "#analogshooters",
    "#analogfever",
    "#analogfromtheworld",
    "#analogarithmic",
    "#analoguelove",
    "#mm",
    "#film",
    "#filmisnotdead",
    "#ishootfilm",
    "#infilmwetrust",
    "#mmfilm",
    "#kodak",
    "#filmcommunity",
    "#filmcamera",
    "#shootfilm",
    "#filmfeed",
    "#believeinfilm",
    "#staybrokeshootfilm",
    "#filmisalive",
    "#grainisgood",
    "#buyfilmnotmegapixels",
    "#keepfilmalive",
    "#mmphotography",
    "#vintage",
    "#lomography",
    "#fujifilm",
    "#filmwave",
    "#istillshootfilm",
    "#theanalogclub",
    "#canon",
    "#kodakfilm",
    "#minolta",
    "#onfilm",
    "#shotonfilm",
    "#filmphotographic",
    "#nikon",
    "#portra",
    "#filmwave",
    "#baeareafilm",
    "#theanalogclub",
    "#believeinfilm",
    "#everybodyfilm",
    "#filmfeed",
    "#filmphotographic",
    "#pulsefilm",
    "#nowherediary",
    "#fujifilm",
    "#filmshooters",
    "#believeinfilm",
    "#onfilm",
    "#filmshooterscollective",
    "#filmcommunity",
    "#bestfilmphoto",
    "#shootitwithfilm",
    "#shootonfilm",
    "#filmshooterscollective",
    "#madewithkodak",
    "#heyfsc",
    "#back2thebase",
    "#kodaklosers",
    "#drivebyfilm",
    "#restorefrombackup",
    "#blurbsonfilm",
    "#deathb4digital",
    "#thefilmpublic",
    "#rolledgoldfilm",
    "#thefilmrenaissance",
    "#photozine",
    "#analogue_people",
    "#shootaesthetics",
    "#filmisgood",
    "kodakprofessional"
    "ilford",
    "ilfordfilm"
    "longlivefilm",
    "filmforever",
    "indiefilmlab",
    "selfdevelopedfilm",
    "#givemefilm",
    "#sharefilm",
    "filmisbetter",
    "#filmneverdies",
    "#filmcolor",
    "#filmonly",
    "#makefilmgreatagain",
    "#negativefb",
    "taintedfilm",
    "#photofilmy",
    "#thefilmgang",
    "#theanalogueproject",
    "#filmday",
    "#camerafilm",
    "#cinefilm",
    "#kodizes",
    "#oftheafternoon",
    "#135film"
]
LIST_MAP[FILM] = film

FILM_FEATURES = 'film_features'
film_features = [
    "#shootfilmmag",
    "#filmphotomag",
    "#photocinematica",
    "#somewheremagazine",
    "#dreamermagazine",
    "#thinkverylittle",
    "#pellicolamag",
    "#classicmagazine",
    "#goldmoony",
    "#analogfeatures",
    "#boxspeedfeature",
    "#makemeseemag",
    "#nowherediary",
    "#senekamagazine",
    "#rentalmag",
    "espritmag",
    "#indiependentmag",
    "#etczine",
    "#missnothingmag",
    "#realismag",
    "#taintedmag",
    "#framepressmag",
    "#theoctobermagazine",
    "#gominimalmag",
    "#tintomag",
    "#verybusymag",
    "#collecmag",
    "#noicemag",
    "#phroommagazine",
    "#paperjournalmag",
    "#aintbadmagazine",
    "#foammagazine",
    "phroom",
    "#yetmagazine",
    "#lucecurated",
    "#lightzine",
    "#justifiedmagazine",
]
LIST_MAP[FILM_FEATURES] = film_features

FILM_35MM = 'film_35mm'
film_35mm = [
    "#35mm",
    "#35mmphotography",
    "#35mmfilmphotography",
    "#35mmstreetphotography",
    "#35mmfilmphoto",
    "#35mmcamera",
    "#35mmphoto",
    "#35mmfilm",
    "#thedaily35mm",
    "35mmbook",
    "35mmwaste",
    "#trip35",
    "#35mm_look",
    "#35mmmagazine",
    "#myfilm35mm",
]
LIST_MAP[FILM_35MM] = film_35mm

FILM_MEDIUM_FORMAT = 'film_medium_format'
film_medium_format = [
    "120film",
    "mediumformatfilm",
    "mediumformat",
    "#120"
    "#hexanon"
    "#bronicatribe"
]
LIST_MAP[FILM_MEDIUM_FORMAT] = 'film_medium_format'

KR_FILM = 'kr_film'
kr_film = [
    "#감성사잔",
    "#필름",
    "#프로필자진",
]
LIST_MAP[KR_FILM] = kr_film

JP_FILM = 'jp_film'
jp_film = [
    "#フィルムカメラ",
    "#フィルム",
    "#フィルムに恋してる",
    "#胶片",
    "#film_com",
    "#film_japan", 
]
LIST_MAP[JP_FILM] = jp_film

RU_FILM = 'ru_film'
ru_film = [
    "#пленка35мм",
    "#пленочнаяфотография",
    "#35mmrussia",
    "#плёнка",
    "#пленочка",
    "#пленкафото",
    "#пленка"
    "#фотонапленку",
    "#фотоназенит"
    "#аналоговаяфотография",
    "#зенитет",
    "#напленку",
    "#зенит12сд",
    "#зенитттл",
    "#зенитфото"
    "#plenkafriends",
    "#35ммплівка",
    "#plenka",
    "#zenitet",
    "#zenit11",
    "#zenet12xp",
    "#zenitphoto",
    "#кодак",
    "#praktica"

]
LIST_MAP[RU_FILM] = ru_film

SPANISH_FILM = 'spanish_film'
spanish_film =[
    "#disparafilm"
    "#argentinaanalogica"
    "#disparaencarrete"
]
LIST_MAP[SPANISH_FILM] = spanish_film
