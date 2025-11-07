Note: The numbers beside certain sentences are citations for the reference list at the bottom of the markdown file.

Introduction: 

    Thallium is among many heavy metals known to be susceptible to uptake by plants from soils through a process known as phytoremediation.(1,2) The expansion of the exploration and extraction of metals is of interest to many as demands for metals increase in industrial, electronic, and energy sectors.3 By understanding the intersection of biology and metals through phytoremediation, an avenue of cost effective, non-invasive metal prospecting and extraction is possible.(1) Furthermore, many metals such as thallium pose health consequences for humans. Thallium has been associated with gastroenteritis, polyneuropathy, alopecia, and death. Therefore, it is also of interest to understand the nature of metals such as thallium in geological and biological systems to maintain human health.(3,4) While many different plants phytoremediate thallium, Brassica juncea (B. juncea), also known also brown mustard, can withsand high concentrations of Tl when it uptakes the metal.(1) For this reason, the phytoremediation of thallium by B. juncea is of particular interest to the IU Metal Isotopes Lab and also the topic of my thesis.

    Thallium has two stable isotopes: 203Tl (29.5%) and 205Tl (70.5%). The relative abundance of 205Tl versus 203Tl is expressed in sigma (ε) notation, where NIST 997 is a thallium standard of the National Institute of Standards and Technology and ε205Tl is the deviation of a sample from the NIST 997 standard:
    ε^205Tl = |( (_^205Tl / _^203Tl)_sample / (_^205Tl / _^203Tl)_(NIST 997) ) - 1| × 10000,
    where 10000 acts as a scaling factor for the ratios.5

    Thallium will fractionate throughout the course of its travel through plants such as B. juncea (the values of ε205Tl will change throughout the plant). This is particularly concerning because elevated ε205Tl levels are associated with higher levels of the Tl3+ thallium ion, which is significantly more toxic to humans than its other common ion Tl+.(6) Data indicate that the exact values of ε205Tl throughout a plant are also dependent on the geology of the substrates they are grown in.1 At the IU Metal Isotopes lab, we are actively acquiring and analyzing these data. 

    As we acquire these data, we are particularly concerned with understanding ε205Tl values in different plant parts of B. juncea. By understanding this, we intend to be able to both predict underlying geology of a site in addition to understanding the health concerns of consuming different parts of the plant. We have currently been growing and harvesting plants in 12-week cycles, producing figures such as Figure 1. Figure 1 shows how ε205Tl from B. juncea will change from soil-to-seedpods for three different geogenic substrates: hendricksite, amazonite, and manganese nodules. One of the next steps for our lab is to monitor ε205Tl throughout plant growth, producing many figures like the one seen in Figure 1. 

    Thus far, Figure 1 and statistical tests have been produced from minimally processed data that are to be used in an upcoming paper by Dr. Shelby Rader. Statistical tests consist of the ANOVA test, pairwise t-test, inter-quartile range test (IQR), and Grubbs test. By using the ANOVA test and pairwise t-test, we are aiming to compare the variability between ε205Tl patterns throughout the plants. The IQR and Grubb’s tests are to test for outliers. Data is currently not structured in a tabular fashion. A figure has also been produced of all, unaveraged ε205Tl data.

![This is what my publication quality figure(s) will look like](/Users/barrettgibbs/Desktop/easg_Data_Analysis/Final_Project/image.png "Figure 1")
 
Project Goals:
    
    The goal of this project is to create a Jupyter Notebook that will automate the creation of figures and all future Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MC-ICP-MS) thallium data analysis. Ideally, both myself and others in the IU Metal Isotopes Lab will be able to simply assign their raw MC-ICP-MS excel file(s) to a string or strings in the Jupyter Notebook, and a plethora of statistical analyses, publication quality graphs, and even an animation can be produced. Publication quality graphs will look very similar to the one already produced from current data, Figure 1. 

    Raw data files include measurements of total Tl beam intensity, raw 205Tl beam intensity, and raw 205Tl/203Tl beam intensity data. All data include errors. In addition to intensity data, normalized 205Tl/203Tl data is present that is calculated by the MS software from intensity data corrected for solution matrix and noise. Data are “bracketed”, meaning that measurements alternate between analyte and standards to correct for instrumental drift. Therefore, extracted data will need to alternate between excel rows. After normalized 205Tl/203Tl data and their errors are extracted, ε205Tl will be calculated from the data above and stored in an n x 3 array with errors and date of harvest. This will look like this: array = np.array([[ε205Tl, error, date_of_harvest], [ε205Tl, error, date_of_harvest], …]).

 Advanced Topic:

    For the advanced topic that I will use, I plan on constructing an animation utilizing parallelization. Although experiments have thus far been completed with one harvest at the end of a twelve-week growth period, one of the next steps for our lab is to monitor Tl concentrations throughout plant growth. A great way that I believe such data could be displayed at a conference would be though an animation of Figure 1 to show the changes of fractionation through time. The days of data acquired would be divided into even increments, and each of these divisions would be assigned a core utilizing Thinlinc to produce figures. Of course, the data that would be used to make this animation has not been produced yet, so made-up “stand-in-data” will be used. 

Timeline: 

    November 12th: Presenting this idea at the geochemistry group meeting to get feedback.
    November 14th: No major additions, as my focus will be on my final touches to the GRFP.
    November 21st: Files can be read in and sorted as the arrays described in “project goals”.
    November 28th: Individual graphs can be produced. This will be an easy step to get to from the data being read-in and stored, so it seems like a good light task for Thanksgiving break. 
    December 5th: Animations can be produced.

References/Sources: 
    (1) Rader, Shelby T., Raina M. Maier, Mark D. Barton, and Frank K. Mazdab. “Uptake and Fractionation of Thallium by Brassica Juncea in a Geogenic Thallium-Amended Substrate.” Environmental Science & Technology 53, no. 5 (2019): 2441–49. https://doi.org/10.1021/acs.est.8b06222.
    (2) Wiggenhauser, Matthias, Rebekah E. T. Moore, Peng Wang, Gerd Patrick Bienert, Kristian Holst Laursen, and Simon Blotevogel. “Stable Isotope Fractionation of Metals and Metalloids in Plants: A Review.” Frontiers in Plant Science Volume 13-2022 (2022). https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.840941.
    (3) Schulz, Klaus, John H. DeYoung Jr., Robert R. Seal II, and Dwight Bradley. Critical Mineral Resources of the United States—An Introduction. Report No. 1802A. Professional Paper, edited by Klaus Schulz, DeYoung Jr., II Seal Robert R., and Dwight Bradley. Reston, VA, 2017. USGS Publications Warehouse. https://doi.org/10.3133/pp1802A.
    (4) WHO/ICPS. “Thallium.” Environmental Health Criteria. 1996.
    (5) Nielsen, Sune, Mark Rehkämper, and Julie Prytulak. “Investigation and Application of Thallium Isotope Fractionation.” Reviews in Mineralogy and Geochemistry 82 (March 2017): 759–98. https://doi.org/10.2138/rmg.2017.82.18.
    (6) Rader, Shelby T., Frank K. Mazdab, and Mark D. Barton. “Mineralogical Thallium Geochemistry and Isotope Variations from Igneous, Metamorphic, and Metasomatic Systems.” Geochimica et Cosmochimica Acta 243 (December 2018): 42–65. https://doi.org/10.1016/j.gca.2018.09.019.
