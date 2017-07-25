# CSP to SDP NIP Data Rates & Data Models (version 1.1)
An ipython notebook and collection of python scripts. These make it easier to model SKA Science Data Processor (SDP)
data rates. Diagrams are included that define the conceptual and logical structure of Non-Imaging Processing (NIP) 
data models. Also included are activity diagrams for all NIP pipelines. Finally, formulas are presented that provide
accurate estimates of NIP pipeline data rates.

## Author: Rob Lyon
## Email : robert.lyon@manchester.ac.uk
## web   : www.scienceguyrob.com

### Overview
This repository consists of, 

* an ipython notebook that explores and describes SDP data models for NIP pipelines.
* diagrams containing Entity-Relationship Models (ERMs), describing the data models/pipeline activity in NIP.
* formulas useful for deriving NIP pipeline data rates.
* standalone unit tested source code, which validates the correctness of the interactive ipython notebook code.

### Notebook

This notebook describes the conceptual and logical data models for the Non-Imaging Processing (NIP) components of the SKA Science Data Processor (SDP), according to [Software Engineering Institute](http://www.sei.cmu.edu) (SEI) standards. The notebook was created for JIRA [TSK-1294](https://jira.ska-sdp.org/browse/TSK-1294), which requested SEI compliant versions of the NIP data models. This document represents the 4th iteration (at least) of the data models work, however only the last two iterations, [TSK-12](https://jira.ska-sdp.org/browse/TSK-12) and [TSK-73](https://confluence.ska-sdp.org/display/WBS/TSK-73+Data+models) are recorded in JIRA. 

All data models presented in this notebook are described via [Entity-Relationship Models](https://en.wikipedia.org/wiki/Entity–relationship_model) (ERMs). These are sometimes referred to as an entity-relationship diagrams (ERDs). There is no standard notation for ERMs, however we have attempted to adhere to defacto standards. Unified Modelling Language (UML) [activity diagrams](https://en.wikipedia.org/wiki/Activity_diagram) are also used to characterise the processing activity within NIP, which ingests and outputs the data models.

This ipython notebook also models the input data rates and data volumes for NIP. It includes models for,

* *pulsar/transient search mode*.
* *pulsar timing mode*.
* *dynamic spectra mode*. The SKA science working group are discussing changing the name of this mode, to better reflect its function. The current name proposed is "Pulsar search filterbank format Data Stream". Please be aware of this, as this change may come into effect after this notebook is finished. The name may even be changed to something entirely different. 

It achieves this through interactive Python 2.7 code. This can be run either within this notebook, or externally via a supplied source code directory. 

Given the use of ERM & UML, basic familiarity with SEI standards is recommended to fully understand the diagrams and terminology used in this notebook.

### License
The code and the contents of this notebook are released under the GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007. We kindly request that if you make use of the notebook, you cite the work appropriately.

### Acknowledgements
This notebook builds upon earlier work by Dr. Lina Levin-Preston & Prof. Ben Stappers. Lina wrote the original data models document, did all the data volume/rate calculations, and provided the original notation! Ben worked on this too. This notebook relies greatly on their earlier work. Thank you Andrea Possenti, for providing valuable feedback which has helped produce the latest version.

### Change log

First version.