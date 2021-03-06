from common.run import run

PERIODICITIES = ["60", "4H", "1D", "3D", "1W"]

# Not all these tickers have been checked for valididty
ASSETS = [
    "OVV",
    "CAR",
    "AR",
    "BJ",
    "CHK",
    "AMC",
    "EGP",
    "PFGC",
    "THC",
    "TTEK",
    "WSC",
    "SWN",
    "M",
    "KBR",
    "STAG",
    "RRC",
    "PDCE",
    "LSCC",
    "IIVI",
    "SWAV",
    "HALO",
    "IRT",
    "INSP",
    "BHVN",
    "TXRH",
    "SSB",
    "RPD",
    "EME",
    "SYNA",
    "SWX",
    "ASGN",
    "SGMS",
    "SAIL",
    "GTLS",
    "SAIA",
    "TRNO",
    "MTDR",
    "MUSA",
    "WCC",
    "MUR",
    "EXPO",
    "HQY",
    "FFIN",
    "TENB",
    "GBCI",
    "RHP",
    "CCMP",
    "LHCG",
    "NSA",
    "ROG",
    "VG",
    "HELE",
    "SIGI",
    "KNSL",
    "OMCL",
    "CMC",
    "ROLL",
    "AQUA",
    "VRNS",
    "BXMT",
    "VLY",
    "ADC",
    "MIME",
    "TGNA",
    "SLAB",
    "KRG",
    "POWI",
    "QLYS",
    "AMN",
    "BKH",
    "UFPI",
    "BIPC",
    "EXLS",
    "POR",
    "MMS",
    "AVNT",
    "SSD",
    "OGS",
    "RLI",
    "NOVT",
    "WK",
    "ALKS",
    "ONB",
    "UBSI",
    "ESNT",
    "ARWR",
    "OPCH",
    "IRDM",
    "CADE",
    "SPSC",
    "HP",
    "LIVN",
    "CHX",
    "ENV",
    "ENSG",
    "HLI",
    "ATKR",
    "BOX",
    "NJR",
    "MEDP",
    "HWC",
    "ITCI",
    "SFBS",
    "SM",
    "ZWS",
    "CNMD",
    "CNX",
    "HGV",
    "BCPC",
    "CWST",
    "UMBF",
    "PNM",
    "HR",
    "ZD",
    "TRTN",
    "CROX",
    "MSTR",
    "PECO",
    "IIPR",
    "LNTH",
    "SMTC",
    "RDN",
    "SIG",
    "APG",
    "IRTC",
    "APLE",
    "DOC",
    "OUT",
    "GATX",
    "APLS",
    "ABG",
    "BPMC",
    "SR",
    "SAFM",
    "AIT",
    "GT",
    "CBT",
    "BL",
    "PSB",
    "TNET",
    "NTLA",
    "SEAS",
    "FLR",
    "WD",
    "FOXF",
    "FELE",
    "LXP",
    "WTS",
    "SMPL",
    "FN",
    "CBU",
    "FUL",
    "NSP",
    "INDB",
    "LTHM",
    "ORA",
    "ONTO",
    "SXT",
    "VRNT",
    "SI",
    "SFM",
    "SJI",
    "PCH",
    "NSIT",
    "KFY",
    "ATI",
    "EBC",
    "MATX",
    "VIAV",
    "HOMB",
    "DBRG",
    "DEN",
    "CARG",
    "PRFT",
    "XTSLA",
    "BNL",
    "SHOO",
    "MMSI",
    "PZZA",
    "JBT",
    "TMHC",
    "PCRX",
    "SUM",
    "CRC",
    "ACIW",
    "MGY",
    "BKU",
    "REZI",
    "HRI",
    "EYE",
    "ABM",
    "BECN",
    "ALE",
    "PEB",
    "CVBF",
    "DIOD",
    "ADNT",
    "AEL",
    "MXL",
    "ETRN",
    "OFC",
    "TWNK",
    "MLI",
    "PPBI",
    "UCBI",
    "ASB",
    "HASI",
    "NWE",
    "MP",
    "CATY",
    "ASO",
    "WBT",
    "SONO",
    "APPS",
    "CELH",
    "WING",
    "EPRT",
    "SFNC",
    "MTH",
    "AWR",
    "FIX",
    "FIBK",
    "NEOG",
    "ESGR",
    "AVA",
    "AJRD",
    "HI",
    "HL",
    "NARI",
    "AMBA",
    "CNO",
    "KLIC",
    "RCM",
    "QTWO",
    "BCO",
    "LANC",
    "CBRL",
    "PTEN",
    "NUVA",
    "BCC",
    "ARVN",
    "AEIS",
    "EQC",
    "WLL",
    "SPT",
    "ALRM",
    "SITC",
    "TRUP",
    "KOS",
    "MGEE",
    "FCFS",
    "FATE",
    "MAC",
    "CWT",
    "CYTK",
    "FORM",
    "MC",
    "STAA",
    "GPI",
    "KRTX",
    "WHD",
    "FHI",
    "PDCO",
    "ENS",
    "CVLT",
    "HAE",
    "SBRA",
    "SKY",
    "PTCT",
    "KW",
    "RMBS",
    "INSM",
    "BE",
    "SITM",
    "OMI",
    "AXNX",
    "ARNC",
    "BOOT",
    "COOP",
    "ITGR",
    "ABCB",
    "AUB",
    "REGI",
    "SHO",
    "TCBI",
    "KBH",
    "OAS",
    "CCOI",
    "BRBR",
    "PGNY",
    "BLKB",
    "ELY",
    "WSFS",
    "IBTX",
    "UNFI",
    "MDRX",
    "ATRC",
    "UNF",
    "PBH",
    "PD",
    "MTSI",
    "DY",
    "ALTR",
    "WDFC",
    "CWEN",
    "CPE",
    "FOCS",
    "ACA",
    "NAVI",
    "CIVI",
    "FULT",
    "VC",
    "UNIT",
    "AIN",
    "LCII",
    "FWRD",
    "ABR",
    "SEM",
    "MOG.A",
    "OTTR",
    "CWK",
    "HLNE",
    "RRR",
    "MAXR",
    "FBP",
    "SAVE",
    "GKOS",
    "ALGT",
    "EPAY",
    "SANM",
    "VSH",
    "PBF",
    "DNLI",
    "MTOR",
    "DORM",
    "NVRO",
    "COLB",
    "YELP",
    "MLKN",
    "AX",
    "BMI",
    "NGVT",
    "ACAD",
    "FRME",
    "RLJ",
    "TRN",
    "GHC",
    "AEO",
    "WERN",
    "UPWK",
    "TEX",
    "CIM",
    "NHI",
    "SHAK",
    "ROIC",
    "EVTC",
    "PRMW",
    "HLIO",
    "JJSF",
    "MNTV",
    "FCPT",
    "COKE",
    "IGT",
    "KMT",
    "AIMC",
    "AAON",
    "IOSP",
    "THRM",
    "NUS",
    "EVH",
    "BDC",
    "RAMP",
    "CVCO",
    "MANT",
    "NTCT",
    "IBOC",
    "BEAM",
    "VRRM",
    "DRH",
    "DOCN",
    "DAN",
    "PLXS",
    "XHR",
    "CPK",
    "ASAN",
    "WLY",
    "CALM",
    "GLNG",
    "UE",
    "TPH",
    "NMRK",
    "CALX",
    "BRC",
    "ITRI",
    "KAI",
    "APAM",
    "WRE",
    "GBT",
    "KWR",
    "HUBG",
    "MED",
    "OCDX",
    "LGIH",
    "ENR",
    "KTB",
    "BDN",
    "BTU",
    "APPF",
    "MDC",
    "PIPR",
    "TROX",
    "PDM",
    "PLAY",
    "ODP",
    "GMS",
    "PRGS",
    "WAFD",
    "WIRE",
    "CMP",
    "FSS",
    "MTX",
    "SCL",
    "GCP",
    "VSTO",
    "RLAY",
    "CBZ",
    "WSBC",
    "CNS",
    "MGRC",
    "OI",
    "CSGS",
    "FOLD",
    "EPC",
    "RUSHA",
    "KTOS",
    "IBP",
    "CSTM",
    "CNNE",
    "ANF",
    "VRTV",
    "FBC",
    "MSGE",
    "NPO",
    "BLMN",
    "IHRT",
    "AMKR",
    "NXRT",
    "CORT",
    "FFBC",
    "ARCH",
    "APPN",
    "KAR",
    "AAWW",
    "TOWN",
    "SPXC",
    "AVAV",
    "MWA",
    "PSMT",
    "JELD",
    "SMCI",
    "HTLF",
    "TWST",
    "EAF",
    "TDS",
    "TSE",
    "DOOR",
    "LKFN",
    "TELL",
    "PRAA",
    "ARCB",
    "ACLS",
    "JOE",
    "GNW",
    "EBS",
    "SASR",
    "JACK",
    "PGRE",
    "VGR",
    "ATSG",
    "CRS",
    "SBCF",
    "ARI",
    "TTGT",
    "AKR",
    "BGS",
    "EAT",
    "OM",
    "CNK",
    "AAT",
    "BCRX",
    "FSR",
    "SSTK",
    "NKLA",
    "SGRY",
    "CAKE",
    "IDCC",
    "ICFI",
    "SKT",
    "TRMK",
    "MD",
    "IRWD",
    "MARA",
    "B",
    "WGO",
    "RNST",
    "HOPE",
    "WWW",
    "STRA",
    "MYGN",
    "BANR",
    "FLYW",
    "THS",
    "CENTA",
    "NEX",
    "RVLV",
    "DEA",
    "PRK",
    "TBK",
    "SBH",
    "SJW",
    "WOR",
    "NTB",
    "POLY",
    "ISEE",
    "DDD",
    "EGBN",
    "USD",
    "URBN",
    "GTN",
    "NG",
    "INT",
    "XPER",
    "TVTX",
    "MEI",
    "PING",
    "HMN",
    "KN",
    "TWO",
    "PFS",
    "AIR",
    "FCEL",
    "BBBY",
    "CSWI",
    "MTRN",
    "AMRC",
    "ESE",
    "VBTX",
    "EFSC",
    "HCC",
    "CTRE",
    "CDNA",
    "HTH",
    "ANDE",
    "RCII",
    "CCS",
    "COUR",
    "NVEE",
    "HNI",
    "NMIH",
    "VCYT",
    "GEF",
    "WABC",
    "PRG",
    "VCEL",
    "LPSN",
    "CVET",
    "EVRI",
    "ETWO",
    "TGI",
    "ALEX",
    "CLDX",
    "MSEX",
    "CXW",
    "PJT",
    "TGH",
    "NOG",
    "NWBI",
    "DDS",
    "GNL",
    "MFA",
    "NWN",
    "LOB",
    "LILAK",
    "MNRO",
    "SKYW",
    "AMEH",
    "RLGY",
    "UCTT",
    "PFSI",
    "LBRT",
    "LRN",
    "LNN",
    "XNCR",
    "ECOL",
    "CRK",
    "BANF",
    "TPTX",
    "OXM",
    "MPLN",
    "PLUS",
    "AVNS",
    "LGF.B",
    "LGND",
    "EXTR",
    "DK",
    "INFN",
    "PMT",
    "ATGE",
    "NBTB",
    "GDOT",
    "VRTS",
    "IPAR",
    "TVTY",
    "KALU",
    "KFRC",
    "LPRO",
    "VRE",
    "CDEV",
    "MYRG",
    "TTEC",
    "ECPG",
    "OSTK",
    "ZUO",
    "MGNI",
    "LC",
    "CRVL",
    "SUPN",
    "ANAT",
    "NNI",
    "TTMI",
    "KRYS",
    "CEIX",
    "PLMR",
    "CASH",
    "NOVA",
    "PACB",
    "PATK",
    "SPWR",
    "CSR",
    "GOLF",
    "GVA",
    "LTC",
    "SWTX",
    "SVC",
    "ENVA",
    "UVV",
    "GBX",
    "PHR",
    "FBK",
    "SILK",
    "ENTA",
    "VIR",
    "SYBT",
    "ADUS",
    "MODV",
    "HCSG",
    "AMPH",
    "IRBT",
    "CFFN",
    "FBNC",
    "RDFN",
    "LADR",
    "AGIO",
    "CUBI",
    "TNC",
    "STC",
    "TRS",
    "SLCA",
    "RVMD",
    "CNR",
    "PRA",
    "WMK",
    "ALG",
    "IMKTA",
    "OSIS",
    "CERE",
    "ROCK",
    "USPH",
    "FCF",
    "MHO",
    "DOMO",
    "ASIX",
    "OFG",
    "APTS",
    "RIOT",
    "MEG",
    "SCHN",
    "SAFT",
    "TBBK",
    "GIII",
    "FROG",
    "VICR",
    "PRIM",
    "HSKA",
    "ARGO",
    "MGPI",
    "ILPT",
    "OII",
    "NEO",
    "ESRT",
    "EFR",
    "DIN",
    "COHU",
    "CDLX",
    "SDGR",
    "SPTN",
    "BKD",
    "EPAC",
    "BUSE",
    "STAR",
    "STEP",
    "LAND",
    "RGR",
    "AVID",
    "DCOM",
    "SFL",
    "PRLB",
    "DNUT",
    "RPAY",
    "UEC",
    "LZB",
    "PRTA",
    "PRO",
    "FLGT",
    "RCUS",
    "RVNC",
    "DLX",
    "NYMT",
    "AROC",
    "PUMP",
    "SNEX",
    "GOGO",
    "CHEF",
    "SBSI",
    "CRNC",
    "TEN",
    "BRP",
    "OPK",
    "UIS",
    "BGCP",
    "KYMR",
    "EIG",
    "FFWM",
    "VECO",
    "CHCO",
    "SXI",
    "NVTA",
    "HRMY",
    "LAUR",
    "ELF",
    "GTY",
    "SKIN",
    "EGHT",
    "HURN",
    "RGNX",
    "RILY",
    "SGH",
    "DNOW",
    "CUTR",
    "BHLB",
    "NXGN",
    "MLAB",
    "HEES",
    "APOG",
    "OCFC",
    "CNOB",
    "BRKL",
    "AZZ",
    "NBHC",
    "NBR",
    "GPRO",
    "TCBK",
    "WOW",
    "FRG",
    "CYH",
    "OPI",
    "KAMN",
    "VIVO",
    "RPT",
    "NTUS",
    "TMP",
    "IMGN",
    "MMI",
    "CTS",
    "TREE",
    "MNRL",
    "BBIO",
    "PCVX",
    "CWH",
    "FIZZ",
    "CCO",
    "EVOP",
    "DRQ",
    "PFC",
    "BIG",
    "NCBS",
    "SHEN",
    "CCXI",
    "DVAX",
    "PRVA",
    "SBGI",
    "CDE",
    "MBUU",
    "GPRE",
    "CMPR",
    "CENX",
    "HCAT",
    "AMCX",
    "EDIT",
    "STBA",
    "BRMK",
    "BANC",
    "CMCO",
    "GSHD",
    "RWT",
    "UMH",
    "SCS",
    "MRTN",
    "CWEN",
    "FRO",
    "CRNX",
    "SHYF",
    "PGTI",
    "CYRX",
    "CDMO",
    "LBAI",
    "AIV",
    "INN",
    "AHCO",
    "ROAD",
    "STNG",
    "CLNE",
    "ONEM",
    "TBI",
    "MCRI",
    "SSP",
    "FA",
    "SNBR",
    "RC",
    "BCOR",
    "BALY",
    "SCHL",
    "HA",
    "MATW",
    "SAFE",
    "AGM",
    "TGTX",
    "KURA",
    "MODN",
    "MCB",
    "TMST",
    "XMTR",
    "MRC",
    "EXPI",
    "PSN",
    "SAH",
    "GES",
    "GABC",
    "CHCT",
    "BKE",
    "BATRK",
    "OEC",
    "GCO",
    "OBNK",
    "LPI",
    "ATRI",
    "RTL",
    "PI",
    "TSC",
    "CNDT",
    "CTKB",
    "AOSL",
    "QCRH",
    "USNA",
    "RDNT",
    "ATRS",
    "MGI",
    "XENT",
    "PAR",
    "MDGL",
    "RADI",
    "NSTG",
    "PLAB",
    "SATS",
    "AHH",
    "GFF",
    "KROS",
    "AMSF",
    "NTST",
    "SUMO",
    "ARRY",
    "AVYA",
    "TUP",
    "GMRE",
    "NHC",
    "INSW",
    "EB",
    "STEM",
    "CCSI",
    "VERU",
    "GLDD",
    "FGEN",
    "NUVB",
    "SNCY",
    "IPI",
    "SMP",
    "HFWA",
    "DBI",
    "ATEN",
    "BIGC",
    "GDEN",
    "DFIN",
    "UTZ",
    "WASH",
    "ANGO",
    "EFC",
    "SCSC",
    "ADTN",
    "AORT",
    "JRVR",
    "FDP",
    "KRNY",
    "LGF.A",
    "ZNTL",
    "ATEC",
    "ASTE",
    "LMAT",
    "HBNC",
    "CLBK",
    "AXSM",
    "HSC",
    "CSII",
    "PTGX",
    "CAL",
    "WRLD",
    "BHE",
    "MNKD",
    "ALHC",
    "SWM",
    "WETF",
    "CARS",
    "RXDX",
    "FARO",
    "IIIN",
    "ICHR",
    "DENN",
    "TWOU",
    "CDXS",
    "SNDX",
    "CERS",
    "RETA",
    "LYEL",
    "EBIX",
    "SRCE",
    "BLNK",
    "DHT",
    "HZO",
    "IMAX",
    "PEBO",
    "ARKO",
    "HLIT",
    "TDW",
    "ERII",
    "CEVA",
    "CPRX",
    "HMST",
    "VREX",
    "PRDO",
    "MYE",
    "XPEL",
    "SAVA",
    "UTL",
    "GOOD",
    "GEVO",
    "NPTN",
    "RXRX",
    "AXL",
    "ABTX",
    "ACRS",
    "SFIX",
    "AGYS",
    "CVI",
    "PLYM",
    "UVSP",
    "INVA",
    "GRC",
    "SLP",
    "HSII",
    "AMWD",
    "SPNS",
    "HWKN",
    "KELYA",
    "TILE",
    "GEO",
    "GSAT",
    "AMTB",
    "CSV",
    "QTRX",
    "ZUMZ",
    "PLOW",
    "WINA",
    "BRY",
    "XPRO",
    "DM",
    "UHT",
    "CAC",
    "JBSS",
    "BRSP",
    "RUTH",
    "LUNG",
    "BSIG",
    "VTOL",
    "CMRE",
    "ACCO",
    "CCRN",
    "VVI",
    "HAFC",
    "RES",
    "AMRS",
    "YEXT",
    "TWI",
    "FBMS",
    "BJRI",
    "SIBN",
    "CTBI",
    "HONE",
    "ROCC",
    "SXC",
    "KIDS",
    "SANA",
    "NAPA",
    "HTBK",
    "PFBC",
    "CLDT",
    "PDFS",
    "AMRK",
    "GDYN",
    "WNC",
    "ARLO",
    "SP",
    "SWBI",
    "ACRE",
    "ACEL",
    "HNGR",
    "SENS",
    "KREF",
    "HLX",
    "DGII",
    "STRL",
    "PWSC",
    "PARR",
    "TRTX",
    "CIO",
    "PLCE",
    "TALO",
    "ACCD",
    "FFIC",
    "NX",
    "RNA",
    "GNK",
    "CHS",
    "LFST",
    "AVXL",
    "CVGW",
    "ARR",
    "GRBK",
    "AMWL",
    "BXC",
    "AAN",
    "CCF",
    "CFB",
    "MORF",
    "CHRS",
    "IMXI",
    "ETD",
    "NTGR",
    "BY",
    "FMBH",
    "NP",
    "ATRA",
    "GSBC",
    "HTLD",
    "CLFD",
    "BFS",
    "CPF",
    "COWN",
    "HIBB",
    "AVD",
    "LOVE",
    "ECVT",
    "FORR",
    "UFCS",
    "PGC",
    "RLMD",
    "ATEX",
    "BAND",
    "ALEC",
    "TCX",
    "INO",
    "SPNT",
    "OFIX",
    "KDNY",
    "BTRS",
    "COLL",
    "VERV",
    "ITOS",
    "RYI",
    "NFBK",
    "MSBI",
    "PACK",
    "LLNW",
    "CATC",
    "TBPH",
    "FUBO",
    "TRST",
    "LTH",
    "CRAI",
    "WSR",
    "LASR",
    "ARQT",
    "MOV",
    "PBI",
    "TMDX",
    "TMCI",
    "DHC",
    "BV",
    "VNDA",
    "AMSWA",
    "RICK",
    "GCI",
    "PETQ",
    "DCO",
    "GPMT",
    "OPRX",
    "CLAR",
    "SGMO",
    "IVR",
    "HCKT",
    "SRDX",
    "BBSI",
    "ALBO",
    "CASS",
    "MITK",
    "GOSS",
    "AGX",
    "ALLO",
    "RXT",
    "MBI",
    "CNXN",
    "CBTX",
    "MXCT",
    "ALX",
    "DHIL",
    "EGRX",
    "IIIV",
    "GOEV",
    "QUOT",
    "NWLI",
    "TRNS",
    "REPL",
    "DX",
    "BMRC",
    "UBA",
    "TR",
    "OSW",
    "RGP",
    "MBWM",
    "WW",
    "CHUY",
    "NSSC",
    "SRNE",
    "SCVL",
    "FSP",
    "MVIS",
    "KZR",
    "REAL",
    "SWIM",
    "INGN",
    "FC",
    "THFF",
    "ASPN",
    "BNGO",
    "BFLY",
    "THR",
    "YORW",
    "GLT",
    "OSPN",
    "ERAS",
    "PTLO",
    "KOP",
    "EGLE",
    "FMNB",
    "QNST",
    "HAYN",
    "CARA",
    "LIND",
    "HIFS",
    "NRC",
    "WKHS",
    "KPTI",
    "VVNT",
    "CSTL",
    "CRMT",
    "FOSL",
    "ENDP",
    "MDXG",
    "SRI",
    "UFPT",
    "TITN",
    "RCKT",
    "MGNX",
    "HRTX",
    "HSTM",
    "OLP",
    "BFC",
    "PNTG",
    "CRGY",
    "LAW",
    "FISI",
    "AGTI",
    "OUST",
    "NGM",
    "TA",
    "BHG",
    "RMAX",
    "VXRT",
    "GRPN",
    "REX",
    "PCT",
    "GERN",
    "HTBI",
    "AVO",
    "PETS",
    "AFMD",
    "BLX",
    "AGEN",
    "MOFG",
    "MTW",
    "OSUR",
    "CPSI",
    "ORGO",
    "MCFT",
    "SPWH",
    "ARCT",
    "FCBC",
    "LXFR",
    "BOC",
    "WTTR",
    "BFST",
    "EQBK",
    "TIL",
    "DOUG",
    "IBCP",
    "BZH",
    "ATNI",
    "OCGN",
    "CARE",
    "USM",
    "ANAB",
    "FNKO",
    "INBX",
    "RIGL",
    "ALTO",
    "JYNT",
    "RMR",
    "CSTR",
    "PAYA",
    "CLW",
    "HYFM",
    "TTI",
    "CENT",
    "HCCI",
    "CRSR",
    "CCB",
    "CNSL",
    "TPIC",
    "RBCAA",
    "TPB",
    "DCPH",
    "UPLD",
    "EBF",
    "AROW",
    "LILA",
    "VSEC",
    "FLIC",
    "KE",
    "CIR",
    "LPG",
    "WTI",
    "DXPE",
    "PMVP",
    "FBRT",
    "BOOM",
    "CCNE",
    "ECOM",
    "PTVE",
    "BW",
    "STGW",
    "MCBS",
    "IDT",
    "VRAY",
    "CTT",
    "VEC",
    "FPI",
    "SRG",
    "MVBF",
    "IAS",
    "ICPT",
    "HVT",
    "WTBA",
    "CTOS",
    "BVH",
    "HYLN",
    "MOD",
    "TTCF",
    "NAT",
    "JOUT",
    "ADV",
    "OSBC",
    "MBIN",
    "FRPH",
    "VERI",
    "LL",
    "STER",
    "BASE",
    "BHB",
    "REVG",
    "ORC",
    "DNMR",
    "NRIX",
    "ALRS",
    "ESTE",
    "RAPT",
    "ULCC",
    "OIS",
    "VPG",
    "PRTY",
    "INBK",
    "AMK",
    "AVIR",
    "GIC",
    "TPC",
    "ABSI",
    "GCMG",
    "NPK",
    "APEI",
    "CRBU",
    "BLFY",
    "AMNB",
    "YMAB",
    "IMGO",
    "UEIC",
    "PAHC",
    "ARTNA",
    "MCS",
    "RAD",
    "DBD",
    "RIDE",
    "MGTX",
    "ONTF",
    "LQDT",
    "AMRX",
    "MPB",
    "EVCM",
    "CZNC",
    "AEVA",
    "SFST",
    "GRWG",
    "INDT",
    "POWW",
    "MCRB",
    "CTO",
    "TRC",
    "SOVO",
    "EOLS",
    "UVE",
    "IDEX",
    "IDYA",
    "ATHA",
    "CMRX",
    "ACET",
    "AMBC",
    "CCCC",
    "HCI",
    "CMTL",
    "FDMT",
    "BWB",
    "MASS",
    "BVS",
    "ALKT",
    "MLNK",
    "TNK",
    "SMBC",
    "WSBF",
    "EZPW",
    "SEER",
    "GLUE",
    "ZEUS",
    "RYTM",
    "NOTV",
    "TCMD",
    "EWCZ",
    "KRO",
    "RM",
    "HNST",
    "TSVT",
    "OFLX",
    "SG",
    "PFIS",
    "SMBK",
    "CCBG",
    "FLWS",
    "VUZI",
    "GEF",
    "SENEA",
    "ESMT",
    "RBB",
    "RSI",
    "FRST",
    "TRUE",
    "DSGN",
    "PRCH",
    "RDUS",
    "ANIP",
    "DMRC",
    "AERI",
    "BSRR",
    "DSKE",
    "STOK",
    "SIGA",
    "INTA",
    "CIVB",
    "TLS",
    "BHR",
    "ONEW",
    "HRT",
    "EBTC",
    "XXII",
    "BGFV",
    "EVC",
    "ANIK",
    "EWTX",
    "NR",
    "HY",
    "SOI",
    "STRO",
    "MAX",
    "AUD",
    "CTLP",
    "HT",
    "SPNE",
    "VITL",
    "IESC",
    "RYAM",
    "WLDN",
    "HBCP",
    "PRTS",
    "PRVB",
    "DJCO",
    "CLSK",
    "FLL",
    "APPH",
    "RUN",
    "FULC",
    "PRAX",
    "FNLC",
    "PLBY",
    "ARAY",
    "AMOT",
    "MLR",
    "KALV",
    "FXLV",
    "CLVS",
    "LEU",
    "TG",
    "OPY",
    "OCUL",
    "GBIO",
    "EYPT",
    "XPOF",
    "TNYA",
    "CATO",
    "MMED",
    "SMMF",
    "CONN",
    "FOR",
    "KNSA",
    "BCOV",
    "BLBD",
    "UTMD",
    "BNFT",
    "DICE",
    "FSBC",
    "ARIS",
    "MSFUT",
    "ESPR",
    "KBAL",
    "MPAA",
    "MRSN",
    "CNTY",
    "PRPL",
    "GNTY",
    "CGEM",
    "SLQT",
    "MRNS",
    "IBRX",
    "PRCT",
    "OOMA",
    "SPFI",
    "IEA",
    "FMTX",
    "AXGN",
    "FLMN",
    "EVER",
    "BLUE",
    "HEAR",
    "PHAT",
    "IRMD",
    "VERA",
    "NWPX",
    "BLI",
    "ENFN",
    "BATRA",
    "VSTM",
    "AKRO",
    "TIPT",
    "INVE",
    "AMTX",
    "FREE",
    "ORRF",
    "MMAT",
    "CINC",
    "OPRT",
    "BRBS",
    "VBIV",
    "ALXO",
    "INSG",
    "DYN",
    "COGT",
    "VTGN",
    "BTAI",
    "ATRO",
    "NKTX",
    "RCKY",
    "RMNI",
    "NRIM",
    "OMER",
    "AMAL",
    "FF",
    "URE",
    "CRDO",
    "NESR",
    "LNDC",
    "AVNW",
    "CURO",
    "TCS",
    "SB",
    "SSTI",
    "BRT",
    "FHTX",
    "GTHX",
    "KODK",
    "SCU",
    "RRBI",
    "PVBC",
    "ITIC",
    "SRRK",
    "PCSB",
    "AKTS",
    "HOV",
    "NVEC",
    "DMTK",
    "ABUS",
    "PKE",
    "AXTI",
    "YELL",
    "MCBC",
    "RRGB",
    "KRUS",
    "CSTE",
    "USLM",
    "SNPO",
    "CVLG",
    "RLGT",
    "PSNL",
    "PSTL",
    "AVDX",
    "PTSI",
    "CVGI",
    "FRBA",
    "EHTH",
    "JNCE",
    "ATLC",
    "KNTK",
    "UFI",
    "LE",
    "CTRN",
    "REPX",
    "KNTE",
    "FSBW",
    "EIGR",
    "DAWN",
    "HBIO",
    "PCYO",
    "INST",
    "ACTG",
    "ORMP",
    "AFCG",
    "JANX",
    "TK",
    "OB",
    "ALTG",
    "GHL",
    "LBC",
    "KRON",
    "RBBN",
    "AJX",
    "ATOM",
    "EGAN",
    "ASLE",
    "DZSI",
    "LAB",
    "GNOG",
    "GNUS",
    "KOD",
    "HOFT",
    "OMIC",
    "ICVX",
    "LOCO",
    "FRBK",
    "CAMP",
    "CBNK",
    "NATR",
    "THRY",
    "STKS",
    "HFFG",
    "NDLS",
    "DGICA",
    "IPSC",
    "NUVL",
    "TLYS",
    "COOK",
    "SGC",
    "VLGEA",
    "LMNR",
    "POWL",
    "RXST",
    "AOUT",
    "GWRS",
    "IMVT",
    "PLPC",
    "LAWS",
    "LUNA",
    "ALT",
    "VMD",
    "WEBR",
    "OTLK",
    "NGVC",
    "GLRE",
    "CIA",
    "RLYB",
    "VRA",
    "XL",
    "MTRX",
    "CLPT",
    "GATO",
    "PLRX",
    "ADGI",
    "CBAY",
    "SGHT",
    "ALDX",
    "CCRD",
    "QMCO",
    "HBT",
    "AGS",
    "ZY",
    "CMBM",
    "BSET",
    "LCUT",
    "FDBC",
    "ZYXI",
    "ATCX",
    "AMSC",
    "HPK",
    "VKTX",
    "LCTX",
    "RCEL",
    "OCN",
    "HRTG",
    "FNA",
    "GAN",
    "TARS",
    "SPPI",
    "VIEW",
    "VTYX",
    "VATE",
    "SCOR",
    "LEGH",
    "CRMD",
    "IMUX",
    "VLDR",
    "DIBS",
    "UDMY",
    "PGEN",
    "ALLK",
    "BLFS",
    "BEEM",
    "BNED",
    "LAZY",
    "CASA",
    "TH",
    "MHLD",
    "APYX",
    "IGMS",
    "AOMR",
    "AVTE",
    "SMSI",
    "ALVR",
    "CECE",
    "DLTH",
    "IKNA",
    "STXS",
    "NODK",
    "URGN",
    "MESA",
    "NCMI",
    "ODC",
    "XOMA",
    "ULH",
    "BBCP",
    "ESCA",
    "CDRE",
    "AHT",
    "LXRX",
    "VOXX",
    "CUE",
    "SPRO",
    "KOPN",
    "CRD",
    "KMPH",
    "ATER",
    "FLXS",
    "DAKT",
    "TALS",
    "JOAN",
    "INFU",
    "NATH",
    "CTMX",
    "EMKR",
    "CTXR",
    "NNBR",
    "GRTS",
    "BYRN",
    "FWRG",
    "ATOS",
    "RELY",
    "ORIC",
    "GBL",
    "PBFS",
    "EAR",
    "VAPO",
    "RMO",
    "AVAH",
    "NGMS",
    "FTCI",
    "ASXC",
    "FRGI",
    "SCWX",
    "ABOS",
    "AKYA",
    "MG",
    "DTIL",
    "LTRPA",
    "XBIT",
    "KVHI",
    "AMTI",
    "GRPH",
    "BH",
    "RENT",
    "IMRX",
    "PZN",
    "CPS",
    "THRX",
    "CLPR",
    "KIRK",
    "ALPN",
    "DS",
    "ITI",
    "PRTK",
    "MPX",
    "FUV",
    "EOSE",
    "TSHA",
    "CURV",
    "ATHX",
    "VOR",
    "TRHC",
    "EPZM",
    "STTK",
    "NMTR",
    "PPTA",
    "HLTH",
    "COCO",
    "TSAT",
    "VIRX",
    "CVM",
    "INNV",
    "MILE",
    "CTSO",
    "REKR",
    "AQB",
    "ADVM",
    "VHC",
    "HGEN",
    "EVI",
    "HOWL",
    "PKOH",
    "DRRX",
    "POM",
    "CRIS",
    "OMGA",
    "SFT",
    "AMLX",
    "NLS",
    "TCRT",
    "TYRA",
    "WLFC",
    "VIA",
    "ACLX",
    "LSEA",
    "PBYI",
    "CDXC",
    "SIEN",
    "MIRM",
    "PASG",
    "VEL",
    "DTC",
    "PSTX",
    "KRT",
    "USX",
    "VRCA",
    "IBEX",
    "TXMD",
    "GTYH",
    "MBII",
    "HQI",
    "TIG",
    "TKNO",
    "SESN",
    "RUBY",
    "ARDX",
    "TNXP",
    "STON",
    "AKBA",
    "REFI",
    "ANNX",
    "AKUS",
    "PAVM",
    "OYST",
    "SELB",
    "EVLO",
    "CNVY",
    "HBB",
    "ICAD",
    "CRTX",
    "DRIO",
    "MEC",
    "VHI",
    "OLMA",
    "FIXX",
    "WVE",
    "FBIO",
    "INFI",
    "DSP",
    "TCRR",
    "INZY",
    "KLTR",
    "CELC",
    "EEX",
    "MTEM",
    "SQZ",
    "RPID",
    "SURF",
    "VALU",
    "SMED",
    "STIM",
    "AGLE",
    "IBIO",
    "WLLAW",
    "LOTZ",
    "SRT",
    "USER",
    "SEEL",
    "AURA",
    "XGN",
    "OCX",
    "AC",
    "HMTV",
    "AIP",
    "FLNT",
    "SBTX",
    "GLSI",
    "NL",
    "BDTX",
    "TRDA",
    "UIHC",
    "TAST",
    "FORA",
    "RVP",
    "UAVS",
    "NBEV",
    "BCEL",
    "MEIP",
    "BMEA",
    "RAIN",
    "FOA",
    "RGS",
    "CDAK",
    "CSSE",
    "CURI",
    "CRDF",
    "AWH",
    "GBOX",
    "QTNT",
    "MBIO",
    "PRLD",
    "BCAB",
    "AMPE",
    "SYRS",
    "CLNN",
    "TRVN",
    "NPCE",
    "SKYT",
    "EBET",
    "ATNX",
    "HARP",
    "HOFV",
    "MGTA",
    "IVC",
    "FREQ",
    "PRTH",
    "SLDB",
    "NLTX",
    "FTHM",
    "NEXI",
    "ONCT",
    "REV",
    "BYSI",
    "TISI",
    "LVO",
    "SMMT",
    "TCBX",
    "PLSE",
    "BOLT",
    "CDZI",
    "CVRX",
    "CIX",
    "ZGNX",
    "AVRO",
    "SNSE",
    "ESGC",
    "GTBP",
    "ADRO",
    "AIRS",
    "KALA",
    "AXDX",
    "APLT",
    "ADN",
    "BTX",
    "ZVIA",
    "VINC",
    "GMTX",
    "DNAY",
    "IMPL",
    "AVTX",
    "TERN",
    "HOOK",
    "ANGN",
    "ALGS",
    "HYRE",
    "MDVL",
    "CYT",
    "ETNB",
    "AKA",
    "SDIG",
    "ONCR",
    "WLLBW",
    "VIGL",
    "XLO",
    "HMPT",
    "PYXS",
    "RFL",
    "PRTG",
    "NH",
    "ELYM",
    "FNCH",
    "SGTX",
    "BDSX",
    "FBRX",
    "SPRB",
    "TLIS",
    "RPHM",
    "LSF",
    "AFIB",
    "OTRK",
    "SERA",
    "DMS",
    "GNLN",
    "LVLU",
    "LABP",
    "ISO",
]


if __name__ == "__main__":
    run(ASSETS, PERIODICITIES, headless=False)
