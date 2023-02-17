# auto_mkdir
The goal of the code is to create directories from a .json input file as seen below. Just need to figure out the logic for dynamic path changes  as the directories are being created. Any help is welcome. 

## The Expected Results

````
root
├── level_1
│   ├── level_1_1
│   │   ├── level_1_1_1
│   │   └── level_1_1_2
│   └── level_1_2
│       ├── level_1_2_1
│       └── level_1_2_2
└── level_2
    ├── level_2_1
    │   ├── level_2_1_1
    │   └── level_2_1_2
    └── level_2_2
        ├── level_2_2_1
        └── level_2_2_2
````

## Current Results
````
root
└── level_1
    └── level_1_1
        ├── level_1_1_1
        ├── level_1_1_2
        └── level_1_2
            ├── level_1_2_1
            ├── level_1_2_2
            └── level_2
                └── level_2_1
                    ├── level_2_1_1
                    ├── level_2_1_2
                    └── level_2_2
                        ├── level_2_2_1
                        └── level_2_2_2
````
