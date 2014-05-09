## The evolution of scaling from the homogeneous era to the heterogeneous era

Mark Bohr
2011/12/5

* Nice paper on scaling of CMOS
* Can use it as a reference for "billions" of transistors on a chip


## Design and simulation of sequential circuits in quantum-dot cellular automata: Falling edge-triggered flip-flop and counter study

Li Cai, Xiaohui Zhao, Nansheng Zhang; 2009

* They do some circuit designs (flipflop, counter) using the QCADesigner program.


## Majority logic gate for magnetic quantum-dot cellular automata

Alexandra Imre, G Csaba, L Ji, A Orlov, GH Bernstein, W Porod
2006/1/13

* Some interesting looking references for circuit design (presumably for QCA)
* More references for MQCA, dating back to 2000! (and not from the Lent group,
  or Notre Dame)
* Nice paper with nice introduction and references! And nice explanation of
  MQCA.
* They experimentally demonstrate a line of "cells" and a majority gate.
* They call the original QCA scheme electrostatic QCA, or EQCA.
* I am not terribly convinced by their experiments. They have structurally fixed
  inputs, the failure rate is quite high.
* They point out that they cannot scale this up to very large devices; and hence
  proposed clocked units with pipelining.


## Clocking scheme for nanomagnet QCA

Mohmmad T Alam, Jarett DeAngelis, Michael Putney, X Sharon Hu, Wolfgang Porod,
Michael Niemier, Gary H Bernstein
2007/8/2




---

(The following is from my paper literature review)

## C. S. Lent, P. D. Tougaw, W. Porod, and G. H. Bernstein, Nanotechnology 4, 49 (1993)

* The original QCA paper.
* Introduces the idea, logical structures, gates; non-linear response / gain. * ICHA is already introduced here. It is not properly verified / motivated. * Starts from a Hubbard model.
* One cell is treated exactly. For more than one cell ICHA is used.
* Introduces cell polarization.


## P. D. Tougaw and C. S. Lent, J. Appl. Phys. 75, 1818 (1994)

* Very similar in content the the original 1993 Nanotechnoloy paper, but goes into more detail.
* In fact, as far as I remember, a lot of the early papers are very similar, overlapping in content.
* Does include numerical values / estimates for used parameters.
* Shows how a wire is “always” fully polarized (uses ICHA, which is not further ex-
plained in this paper).
* Explores more complex, larger digital devices and structures.


## C. S. Lent and P. D. Tougaw, J. Appl. Phys. 74, 6227 (1993) “Lines of interacting quantumdot cells: A binary wire”

* Another of the very early papers. Again, very overlapping with the other papers.
* Actually, parts of this paper are the same word by word as the 1993 Nanotechnology
paper.
* Again, uses and explains ICHA. But, again, ICHA is not properly verified.
1
* Discusses wire polarization, saturation polarization, how the polarization decays from cell-to-cell; for different parameters. However, it’s all with the ICHA approximation.
* They find that for some parameters, polarizations decay to zero, but in all other cases they find a stable wire polarization (“saturation polarization”). Only the magnitute
of the saturation polarization depends on the choses parameters.
* They show saturation polarization over hopping parameter t and see a clear phase transition where Psat jumps from zero to a non-zero value. — This graph is very
similar to my mean field graphs (I plotted over V1.)
* Note: Their calculations are all for the groundstate
* They do use concrete estimates for their parameters.


## My notes from January 20, 2011

Read Lent paper “Dynamic behaviour in quantum cellular automata” (1996)
in detail. Looked over a lot of the early Lent papers (1993-2001).

* They almost always loook at the ground state
* TheyuseIntercellularHartreeApproximation(ICHA)forvirtuallyakktime-independent
calculations
* As far as I can tell nobody gas ever even attenoted to verify that the ICHA mean
field approach is a good, valid approximation
* Single cell with external driver: Non-linear cell-cell response, gain
* ICHA retains this picture for larger systems (e.g. wire)
* Emerging physical picture: Wire is always fully polarized
* This picture is used repeatedly to illustrate the advantage of QCA and motivate other
approximations (e.g. 2-state approximation)
* This is the mental picture that is used for QCA throughout (and it is not really
correct!)
* 2-state basis is introduced to handle dynamics for larger systems
* 2-statebasisismotivatedbybistablenatureofcells(emergingfromtheICHApicture)
* 2-state basis is verified, although I am not convinced how exact and conclusive their
verification is
* 2-state basis is mapped to the Ising model
* Interestingly, there’s a 2001 J Appl Physics paper discussing the importance of cor-
relations and the breakdown of the ICHA for dynamics.
* Are the ICHA and the 2-state approximation valid and if yes in which parameter
regime?


## P. D. Tougaw and C. S. Lent, J. Appl. Phys. 80, 4722 (1996) “Dynamic behavior of quantum cellular automata”

* This is the paper referred to in my notes from 2011 above.
* I believe this is the paper that originally introduced the 2-state basis.
* Briefly discusses dynamics with ICHA — They show that it is not really correct.
* 2-state basis is motived by picture emerging fomr ICHA (bistable cells)
* 2-state basis is verifed for one cell (time independent) and for three cells (dynamics);
but apparently only for one set of parameters
* Maybe I am missing it, but I don’t think they say what parameters specifically they
are using.
* I believe they only look at the groundstate
* Their full model is a 16 state basis (spin-zero sector, 2 electrons)
* Funnily enough, in their 2-state time-dependent plot it indeed looks like the polar-
izations are decaying from cell to cell
* Discusses dynamics of majority gate, wire, semi-infinite wire.


## Marco’s 2013 paper

"Consequences of Many-cell Correlations in Clocked Quantum- dot Cellular
Automata" has a really nice overview of the commonly used approximations, ICHA
and 2-state (and relaxation time approximation, which I am not interested in),
and discussed them in some detail. Also has good collection of references.

* Interestingly, they also repeatedly reference the 1996 Lent paper for the approxima- tions.
* Includes nice and brief sections on 2-state approximation and ICHA approximation
* Shows that ICHA is wrong even for a simple 2 cell wire.
* “Full quantum mechanical calculation” = 2-state basis, only nearest-neighbour in-
teraction
* Shows in detail the shortcomings of ICHA
* Goes into depth on dynamics, time-evolution, clocking
* “The simulations performed in this work clearly iden- tify depolarization due to
quantum correlations as a crit- ical issue for classical computation using clocked QCA at the molecular and atomic scale. To our knowledge, this phenomenon has not been acknowledged in any of the previous work on QCA.”
* Interestingly, their graphs don’t show any decrease in polarization along the wire (I mean static, not time-dependent)
* They discuss how ICHA works, in some limits, for non-molecular QCA implemen- tations (apparently this was shown experimentally) — although here, as they point out, the device basically operates in the classical regime.


## Enrique P. Blair and Craig S. Lent; Journal of Applied Physics 113, 124302 (2013); “Environmental decoherence stabilizes quantum-dot cellular automata”

* most recent paper by Craig Lent
* nice references; nice introduction
* I read this paper as an answer and dispute to Marco’s 2013 paper
* The basic question is quite interesting: How does information storage, quantum
coherence and decoherence from the environment interact
* Essentially, they argue that decoherence due to interaction with the environment
stabilizes the (classical) QCA bit and surpresses oscillations.
* However, all of this is for a system decoupled from input and hence does not really
apply to or relate to my work.
* I think they have the clocked QCA approach in mind (where you regularly decouple
the input)


## G. Toth and C. S. Lent, J. Appl. Phys. 89, 7943 (2001) “Role of correlation in the operation of quantum-dot cellular automata”

A lot of the later papers (e.g. after 2000) focus on dynamics, power dissipation and clocking.


## A. O. Orlov, I. Amlani, G. H. Bernstein, C. S. Lent, and G. L. Snider, Science 277, 928 (1997) “Realization of a functional cell for quantum-dot cellular automata”

* first experimental realization
* one single cell
* metal islands = quantum dots


## C. S. Lent and P. D. Tougaw, “A device architecture for computing with quan- tum dots,” Proc. IEEE 85, 541–557 (1997).

* This seems to be a nice early review paper. Haven’t looked at it in detail yet.


## Rahimi and Nejad Nanoscale Research Letters 2012, 7:274 “Quasi-classical modeling of molecular quantum-dot cellular automata multidriver gates”

* focuses on molecular QCA (mQCA) which I know little about, has a nice list of references for mQCA
* discusses 2-dot QCA cells, which was new to me
* 2-dot cell: a dipole; QCA circuits are in a plane, where the dipols stand vertically;
thus it’s kind of 3D
* They derive what look’s like a 2-state mean field model and compare it to the exact
quantum chemistry calculations for their molecules; I don’t understand the details.


## Berstein, Porod, 2005. “Magnetic QCA systems”
* I believe this is the first magnetic QCA paper. 


## Molecular QCA papers:

* Craig S. Lent , Beth Isaksen , and Marya Lieberman; J. Am. Chem. Soc., 2003, 125 (4), pp 1056–1063; DOI: 10.1021/ja026856g; “Molecular Quantum-Dot Cellular Automata”
* Yuhui Lu1, Mo Liu1 and Craig Lent, J. Appl. Phys. 102, 034311 (2007); http://dx.doi.org/10.1063/1.2767 Molecular quantum-dot cellular automata: From molecular structure to circuit dy-
namics
* Rahimi and Nejad Nanoscale Research Letters 2012, 7:274; Quasi-classical modeling of molecular quantum-dot cellular automata multidriver gates


## Clocking papers:

* The first paper to introduce clocking: CS Lent, PD Tougaw “A device architecture for computing with quantum dots”; PROCEEDINGS OF THE IEEE, VOL. 85, NO. 4, APRIL 1997 — actually this is a very nice, long paper, with lots of details.
* Hennessy K, Lent CS: Clocking of molecular quantum-dot cellular automata. J Vac Sci Technol B 2001, 19:1752–1755.
* C. S. Lent and B. Isaksen, “Clocked molecular quantum-dot cellular automata,” IEEE Trans. Electron Devices 50, 1890–1896 (2003).
* ??? E. P. Blair and C. S. Lent, in Proc. of the Third IEEE Conference on Nan- otechnology (2003) pp. 402–405. “An architecture for molecular computing using quantum-dot cellular automata”


## Complex ciruits papers:

From Rahimi, 2012: “Several QCA circuits including combinational as well as
sequential circuits have been studied using QCADesigner. Examples are adders,
shift registers, RAM, digital data storage, and simple microprocessors”

* Lent CS, Tougaw PD: A device architecture for computing with quantum dots. Proc of the IEEE 1997, 85:541–557. (Includes adder circuit.)
* Rahimi E, Nejad SM: Quantum-Dot Cellular ROM: A nano-scale level approach to digital data storage. 6th IEEE Int Conf on Communication Systems, Networks and Digital Signal Processing 2008, 618–621.
* Orlov AO, Kummamuru R, Ramasubramaniam R, Lent CS, Bernstein GH, Snider GL: Clocked quantum-dot cellular automata shift register. Surf Sci 2003, 532– 535:1193–1198.
* QCADesigner: Walus K, Dysart TJ, Jullien GA, Budiman RA: QCADesigner: a rapid design and simulation tool for quantum-dot cellular automata. IEEE T Nan- otechnol 2004, 3:26–31.


## Experimental realization papers:
* A. O. Orlov, I. Amlani, G. H. Bernstein, C. S. Lent, and G. L. Snider, Science 277, 928 (1997) “Realization of a functional cell for quantum-dot cellular automata”
* Evidence for transfer of polarization in a quantum dot cellular automata cell con- sisting of semiconductor quantum dots; ..., CG Smith, J Cooper, DA Ritchie, EH Linfield, Y Jin - Physical Review B, 2003 - APS (GaAs/AlGaAs)
    * single cell
* Demonstration of a silicon-based quantum cellular automata cell; ..., RP Starrett, E Gauja, R Brenner, RG Clark. . . - Applied physics . . . , 2006 - scitation.aip.org (Silicon)
    * single cell
    * metallically doped (n+) phosphorus-implanted nanoscale dots / ion-implanted phosphorus-doped silicon (Si:P)
* Wolkow group
* Molecular quantum cellular automata cells. Electric field driven switching of a silicon surface bound array of vertically oriented two-dot molecular quantum cellular ...; H Qi, S Sharma, Z Li, GL Snider, AO Orlov... - Journal of the ..., 2003 - ACS Publications
    * calling this an experimental realization might go a bit far
* My impression is that there is no genuine experimental realization for these molecular systems. But maybe I am wrong. After all, for example the Silicon surface system is also not really a fully working QCA system.
* Experimental realizations of more complex systems (i.e. more than one cell)
    * Quasiadiabatic switching for metal-island quantum-dot cellular automata; G Tth, CS Lent - Journal of Applied physics, 1999
    * Orlov AO, Kummamuru R, Ramasubramaniam R, Lent CS, Bernstein GH, Snider GL: Clocked quantum-dot cellular automata shift register. Surf Sci 2003, 532–535:1193–1198.
        * an experimental shift register


# Theorecical papers / Books

Definitely look at those in detail:

* Operation of quantum cellular automaton cells with more than two electrons; M Girlanda, M Governale, M Macucci, G Iannaccone - Applied physics letters, 1999
* Analysis of polarization propagation along a semiconductor-based quantum cellular
automaton chain; M Girlanda, M Macucci - Journal of applied physics, 2002 6
* Quantum Cellular Automata; M Macucci - 2006 (Chapter in a book)


# General beyond-CMOS

Very interesting March Meeting 2014 session: Session T23: Invited Session:
Industrial Physics Forum: Device Physics at the Nanoscale
Transcribed notes from that session:

* Supriyo Datta, Spin Transistor
    * 2 main characteristics of transistors
        * isolation (output does not influence input)
        * gain
        * (both is not the case for QCA)
    * Spin Transistor uses regular currents, spin is internal variable
    * uses Giant Spin Hall effect
    * non-equilibrium
    * aimed at supplementing CMOS
    * structure of uses magnetic tunnel junctions is quite complicated
    * papers:
        * Behin-Aein, Behtash, et al. “Switching energy-delay of all spin logic de- vices.” Applied Physics Letters 98.12 (2011): 123510.
        * Srinivasan, Srikant, et al. “All-spin logic device with inbuilt nonreciprocity.” Magnetics, IEEE Transactions on 47.10 (2011): 4026-4032.
        * Camsari, Kerem Yunus, Deepanjan Datta, and Supriyo Datta. “Four com- ponent conductance formulation of coherent spin currents.” arXiv preprint arXiv:1402.7055 (2014).


* Dmitri Nikonov, Intel, Benchmarking emerging logic devices
    * Overview study of beyond CMOS
    * two papers: 2012 and 2013
        * Uniform methodology for benchmarking beyond-CMOS logic devices; DE Nikonov, IA Young; Electron Devices Meeting (IEDM), 2012 IEEE Inter- national, 25.4. 1-25.4. 4
        * Overview of beyond-CMOS devices and a uniform methodology for their benchmarking; DE Nikonov, IA Young; IEEE (2013)
    * output of device needs to be the same computatoinal variable and range as input; otherwise we need a transducer
    * Spintronics: Could not get rid of charge; i.e. they need charge / current to make these devices work (for now)
    *
    * Spintronics / CMOS: there is an energy barrier between the two logical states (and that’s not the case for QCA)
    * all presented approaches are current-based
    * “Elliptic Spin Torque Majority Gate”; faster than transitor logic, more versatile
    *n functionality than a traditional transistor (=> different cicuit design)
    * their study found as the most promising beyond-CMOS devices: Spintronics, tunnel-junction based devices


* Tsu-Jae King Liu, Berkeley, Mechanical switches
    * Why back to mechanical switches (relays)?
        * no leakage (but still uses currents when on)
        * low energy
        * intelligent devices (houses, kitchen, environment)
        · does not matter that much, that it is very slow
        * easy, cheap to manufacture
        * they are called MEM (Microelectromechanical Systems)
    * Papers; maybe these:
        * Design, optimization, and scaling of MEM relays for ultra-low-power digital logic;HKam,TJKLiu,VStojanovic... -... IEEETransactionson,2011 
        * Demonstrationofintegratedmicro-electro-mechanicalrelaycircuitsforVLSI applications; . . . , A Gupta, H Kam, V Pott, J Jeon, TJK Liu. . . - Solid- State Circuits, . . . , 2011 - ieeexplore.ieee.org


* Allan H. MacDonald, Texas, Many-Body Switches
    * Nandi et al., PRB 2013
