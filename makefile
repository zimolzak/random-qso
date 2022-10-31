.PHONY: clean

arrl-ss.mp3: arrl-ss.txt
	/Users/ajz/Documents/ebook2cw-0.8.4/ebook2cw -o arrl-ss -c - -w 20 -e 17 $<

arrl-ss.txt: generate_arrl_ss.py main.py arrl-sections.csv
	python $< > $@

clean:
	rm -f arrl-ss.txt arrl-ss.mp3
