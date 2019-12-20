## Level file instructions


### Structure

* Always start the file with "/map" (indicates the start of the level data)
* Separate the characters with a dash ("-")
* Use "." as an empty block (default option, other alternatives work too)
* Use only 1 character per gap between dashes (multiple characters will lead to ignoring the block)
* Recommendation: the level should be at least 25 by 14 non-dash characters [(25 * 64px) * (14 * 64px) = game screen size (1600 * 896)]
* The width of the level is determined by the last line's length


### Dictionary

	P*  =   Player
	X*  =   Goal            (catnip)
	f   =   Floor element   (collideable item)
	g   =   Ground element  (collideable item)
	C   =   Crate element   (collideable item)
	c   =   Cloud element   (non-collideable item, decoration)
	B   =   Bucket element  (static enemy, trigger from above)
	E   =   Enemy           (moving enemy, trigger from below/sides, functions also as a moving platform)
	F   =   Flying enemy    (same as above, animated)
	M   =   Mega Noonoo     (big moving platform)
	p   =   Pipe            (functions as a starting point accessory/decoration)

Any other character will be ignored while reading level data

*Required in a level file

#### Example:

	/map
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-C-.-.-.-.-.-.-.-.-.
	.-.-.-P-.-.-.-C-.-.-.-E-.-.-.-C-B-.-.-.-.-X-.-.-.
	f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f-f
	g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g-g
