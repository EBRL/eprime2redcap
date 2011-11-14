### Export Data

-   Open .edat/.edat2 file in E-DataAid
    -   For .edat2 files, you may need to right-click on the file, select "Open with..." and find E-DataAid.
-   Click on File > Export
-   In the "Export" window that appears, choose "Other" as the "Export to:" option.
-   Make sure of these settings:
    -   Include comments: unchecked
    -   Include column names: checked
    -   Included column flags: unchecked
    -   Missing Data: '.' (the period)
    -   Begin comment: None
    -   End comment: None
    -   Variable separator: \t (Tab)
    -   Data separator: \t (Tab)
    -   Begin data line: None
    -   End data line: @
-   Click "OK" and follow the naming convention below to name the next .txt file
-   Move the file to the correct place on ACCRE.
    -   The correct place is TBD until we have the set "new-server" file structure.

### Naming convention

Because we're going to (at some point hopefully soon) have an automated system to compute statistics on the exported e-prime files and transfer that information into Redcap, a sane and agreed-upon naming convention for the files is **required**.

Why is it required, you ask?  With a known naming convention for e-prime files, we can assume that the filename gives us (correct!) information that we can use to decide which grant, task, and subject this data belongs to, since that data is not in the e-prime data itself.

So, we'll use the following naming convention for the exported files:

`[PROJECT]_[TASK]_[BEHAVID]_[SCANID]_[EXTRA].txt`

Where:

-   [PROJECT] is one of the following:
    -   "NF" for the NFRO1 in-magnet tasks.
    -   "NFB" for NFRO1 out-of-magnet tasks.
    -   "RCV" for the new, Vanderbilt-only ReadingComp grant.
    -   "RCVB" for out-of-magnet RC tasks
    -   "LERD" for the Late-Emerging RD grant (in-magnet tasks).
    -   "LERDB" for out-of-magnet LERD behavioral tasks.
    -   "LMS" for the Last-Minute Study
    -   "LDRC1" for LDRC project 1.
-   [TASK] is one of the following:
    -   "SWR" for Single-Word Reading
    -   "MI" for Mental Imagery
    -   "PIC" for the Pictures Task
    -   "REP" for the Repetition Task
    -   "SENT" for the (out-of-magnet, behavioral) Sentence Comp Task (RCV, NF)
    -   "NBACK" for the N-Back Task
    -   "MR" for the Mental Rotation Task
    -   "OLSON" for the Olson task (LERD, NF)
-   [BEHAVID] is generally a three-digit number( `002`, eg)
    -   NF: studyid_subjscanid (the redcap keys)
    -   NFB: studyid (the NF redcap key) 
    -   LDRC1: 
    -   RCVB: participant\_id, which is really behavid\_scanid
-   [SCANID] is a 4- or 6-digit number that corresponds to the subject's scan ID.
-   [EXTRA] is optional, but could include list versions, pre/post, etc. and will be used only when necessary. The exact use of this field will be grant-specific. See below.

### EXTRA

#### NF (In-Magnet Tasks)

The SWR and PIC tasks should be named as so:

`NF_[TASK]_[SUBJECTID]_[TIME]_[LIST].txt`

where TIME is:

-   Pre
-   Post

and LIST is:

-   ListA
-   ListB

For example, the PIC data from subject 1's (whose scanid is 000000) pre test will be named:

`NF_PIC_1_000000_Pre_ListA.txt`

The MI task has the same list Pre and Post, and thus only needs to be, for example:

`NF_MI_1_000000_Pre.txt`


### File Directories

#### ReadingComp (out-of-magnet) tasks

The only task in this project is the SentComp task, so all files should go to `(Team Drive)/Team Drive/EBRL/Reading Comprehension/Behavioral EPrime/SENTCOMP`

#### LERD (out-of-magnet) tasks

The only task in this prject is the Olson task, so all files should go to:
`(Team Drive)/Team Drive/EBRL/LERD/Behavioral EPrime/OLSON`




### Questions

If you have questions, please email Nikki and/or Scott.
