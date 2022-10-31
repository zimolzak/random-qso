.PHONY: all clean

files = arrl-ss.txt arrl-ss.mp3
ebook2cw = /Users/ajz/Documents/ebook2cw-0.8.4/ebook2cw  # pathname of your executable
wpm = 20
farns = 17
ebookopts = -c - -w $(wpm) -e $(farns)  # "-c -" means no chapter num

all: $(files)

%.mp3: %.txt
	$(ebook2cw) $(ebookopts) -o $* $<

%.txt: generate_arrl_ss.py main.py arrl-sections.csv
	python $< > $@

clean:
	rm -f $(files)
