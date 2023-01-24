# Pdf Miner commands

```
pdf2txt.py [-P password] [-o output] [-t text|html|xml|tag]
             [-O output_dir] [-c encoding] [-s scale] [-R rotation]
             [-Y normal|loose|exact] [-p pagenos] [-m maxpages]
             [-S] [-C] [-n] [-A] [-V]
             [-M char_margin] [-L line_margin] [-W word_margin]
             [-F boxes_flow] [-d]
             input.pdf ...
```

- -P password : PDF password.
- -o output : Output file name.
- -t text|html|xml|tag : Output type. (default: automatically inferred from the output file name.)
- -O output_dir : Output directory for extracted images.
- -c encoding : Output encoding. (default: utf-8)
- -s scale : Output scale.
- -R rotation : Rotates the page in degree.
- -Y normal|loose|exact : Specifies the layout mode. (only for HTML output.)
- -p pagenos : Processes certain pages only.
- -m maxpages : Limits the number of maximum pages to process.
- -S : Strips control characters.
- -C : Disables resource caching.
- -n : Disables layout analysis.
- -A : Applies layout analysis for all texts including figures.
- -V : Automatically detects vertical writing.
- -M char_margin : Speficies the char margin.
- -W word_margin : Speficies the word margin.
- -L line_margin : Speficies the line margin.
- -F boxes_flow : Speficies the box flow ratio.
- -d : Turns on Debug output.


[source: pdf-miner](https://pypi.org/project/pdfminer/)