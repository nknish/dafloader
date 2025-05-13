# dafloader — download the talmud

grab [tzurat hadaf](https://en.wikipedia.org/wiki/Vilna_Edition_Shas) layout images from [daf yomi](https://www.dafyomi.org) site and convert them to a pdf.

so far, it:
- only works on [masechet shabbat](https://en.wikipedia.org/wiki/Shabbat_(Talmud))
- doesn't verify the validity of folio numbers
- downloads a bunch of individual images
- doesn't have a frontend

eventually, it should:
- work for any masechet (ideally with autocomplete to account for inconsistencies in transliteration)
- only accept valid daf numbers (e.g. starting at 2a, ending when the masechet ends)
- convert the images into a single pdf (using [img2pdf](https://pypi.org/project/img2pdf/))
- have a frontend?
