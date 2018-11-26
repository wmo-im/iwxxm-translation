# IWXXM Translation Suite
A repository of examples of IWXXM and Traditional Alphanumeric Code (TAC) message pairs that are deemed to be equivalent. As a body these examples represent
a set of IWXXM and TAC messages that a tool may expected to be able to translate exactly,
other than whitespace and newlines differences.  This repository is provided by the WMO Task Team for Aviation XML (TT-AvXML)
as a convenience for IWXXM developers, but the contents are not reviewed for correctness by TT-AvXML and has no official status in WMO or ICAO.

Messages are provided for each amendment of ICAO Annex 3, as both the TAC and IWXXM contents may change during each
amendment.  Every XML file should contain an equivalent TAC text as the first line (other than the XML header) in a comment by itself.

# Contributing
Pull requests with additional cases are both welcomed and encouraged.  File names should indicate the unique aspects
of the message and should contain the corresponding TAC.  The format for TAC and other information is shown below.

```XML
<!--
History, provenance, and other information about the file go here.
This can extend to multiple lines down to the 'TAC:' delimiter below

TAC:
THE MULTILINE TAC MESSAGE STARTS HERE
AND CONTINUES HERE UNTIL THE END OF THE XML COMMENT BLOCK
-->
<iwxxm:Report />
```
The comments in these XML documents are for illustrating how TAC forms (or portions thereof) are realized in IWXXM XML. There should
be no expectation that such comments will appear in operational IWXXM XML products produced by member states.

# TAC Guidelines
Only ICAO-compliant TAC messages will be accepted into this repository.  There are many TAC messages being produced that have formatting errors, regional content, and other issues that can not be represented in IWXXM.  The focus of this repository is on standard ICAO data exchanges.
