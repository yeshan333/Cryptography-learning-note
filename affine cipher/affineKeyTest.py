# This program proves that the keyspace of the affine cipher is limited
# to len(SYMBOLS) ^ 2.
# 验证仿射加密法并不可靠，Key A，Key B （callback problem）

import affineCipher, cryptomath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 100):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))


# result，3 is equal to 98，.....
""" 
2 {DXL!jRT^Ph!Dh!hT\bZL!Dh!b`hhTFZL9!Flj!^`j!hT\bZLf=
3 I&D2!_;>M8\!&\!\>JSG2!&\!SP\\>)G2E!)b_!MP_!\>JSG2YK 
4 vg0w!T$(< P!gP!P(8D4w!gP!D@PP(k4wQ!kXT!<@T!P(8D4wLY 
6 q+gC!>U[yO8!+8!8[s&mC!+8!& 88[1mCi!1D>!y >!8[s&mC2u 
7 ?lS)!3>Eh7,!l,!,EavZ)!l,!vo,,EsZ)u!s:3!ho3!,EavZ)%$ 
8 lN?n!('/W~ !N ! /OgGn!N !g_  /VGn"!V0(!W_(! /OgGnw2 
9 :0+T!|oxFfs!0s!sx=X4T!0s!XOssx94T.!9&|!FO|!sx=X4Tj@ 
11 5Sb !fAL$6[!S[![Lx:m !S[!:/[[L^m F!^qf!$/f![Lx:m P\
12 b5Ne![*6r}O!5O!O6f+Ze!5O!+~OO6AZeR!Ag[!r~[!O6f+ZeCj
13 0v:K!Pr aeC!vC!C T{GK!vC!{nCC $GK^!$]P!anP!C T{GK6x
14 ]X&1!E[iPM7!X7!7iBl41!X7!l^77if41j!fSE!P^E!7iBl41)'
16 X{]\!/-=.|~!{~!~=}Nm\!{~!N>~~=,m\#!,?/!.>/!~=}Nm\nC
17 &]IB!$u'|dr!]r!r'k?ZB!]r!?.rr'nZB/!n5$!|.$!r'k?ZBaQ
18 S?5(!x^pkLf!?f!fpY0G(!?f!0}ffpQG(;!Q+x!k}x!fpY0G(T_
21 {DX9!Wx.8cB!DB!B.#bm9!DB!bMBB.Ym9_!YlW!8MW!B.#bm9-*
22 I&D~!Law'K6!&6!6wpSZ~!&6!S=66w<Z~k!<bL!'=L!6wpSZ~ 8
23 vg0d!AJau3*!g*!*a^DGd!g*!D-**a~Gdw!~XA!u-A!*a^DGdrF
24 DI{J!63Kdz}!I}!}KL54J!I}!5|}}Ka4J$!aN6!d|6!}KL54JeT
26 ?lSu! d~BJe!le!e~(vmu!le!v\ee~'mu<!': !B\ !e~(vmuKp
27 lN?[!tMh12Y!NY!YhugZ[!NY!gLYYhiZ[H!i0t!1Lt!YhugZ[>~
28 :0+A!i6R yM!0M!MRcXGA!0M!X<MMRLGAT!L&i! <i!MRcXGA1-
29 gqv'!^~<naA!qA!A<QI4'!qA!I,AA</4'`!/{^!n,^!A<QI4'$;
31 b5NR!HPoL1)!5)!)o-+mR!5)!+k))oTmRx!TgH!LkH!)o-+mRiW
32 0v:8!=9Y;x|!v|!|Yz{Z8!v|!{[||Y7Z8%!7]=!;[=!|Yz{Z8\e
33 ]X&}!2"C*`p!Xp!pChlG}!Xp!lKppCyG}1!yS2!*K2!pChlG}Os
34 +:qc!'j-xHd!:d!d-V]4c!:d!];dd-\4c=!\I'!x;'!d-V]4cB"
36 &]I/!p<`VwL!]L!L`2?m/!]L!?zLL`"m/U!"5p!Vzp!L`2?m/(>
37 S?5t!e%JE_@!?@!@J 0Zt!?@!0j@@JdZta!d+e!Eje!@J 0ZtzL
39 Nbl@!OV}#/(!b(!(}[q4@!b(!qJ((}*4@y!*vO!#JO!(}[q4@`h
41 I&Dk!9(Q`^o!&o!oQ7Smk!&o!S*ooQOmk2!Ob9!`*9!oQ7SmkF%
42 vg0Q!.p;OFc!gc!c;%DZQ!gc!Dycc;2ZQ>!2X.!Oy.!c;%DZQ93
43 DI{7!#Y%>.W!IW!W%r5G7!IW!5iWW%tG7J!tN#!>i#!W%r5G7,A
44 q+g|!wBn-uK!+K!Kn`&4|!+K!&YKKnW4|V!WDw!-Yw!Kn`&4|~O
46 lN?H!asBjE3!N3!3B<gmH!N3!g933B|mHn!|0a!j9a!3B<gmHdk
47 :0+.!V\,Y-'!0'!',*XZ.!0'!X)'',_Z.z!_&V!Y)V!',*XZ.Wy
48 gqvs!KEuHtz!qz!zuwIGs!qz!IxzzuBGs'!B{K!HxK!zuwIGsJ(
49 5SbY!@._7\n!Sn!n_e:4Y!Sn!:hnn_%4Y3!%q@!7h@!n_e:4Y=6
51 0v:%!*_3t,V!vV!V3A{m%!vV!{HVV3Jm%K!J]*!tH*!V3A{m%#R
52 ]X&j!~H|csJ!XJ!J|/lZj!XJ!l8JJ|-ZjW!-S~!c8~!J|/lZju`
53 +:qP!s1fR[>!:>!>f|]GP!:>!](>>foGPc!oIs!R(s!>f|]GPhn
54 X{]6!hyPAC2!{2!2PjN46!{2!Nw22PR46o!R?h!Awh!2PjN46[|
56 S?5a!RK$~ry!?y!y$F0ma!?y!0Wyy$wma(!w+R!~WR!y$F0maA9
58 Nbl-!<|W\Ba!ba!aW"qG-!ba!q7aaW=G-@!=v<!\7<!aW"qG-'U
59 {DXr!1eAK*U!DU!UAob4r!DU!b'UUA 4rL! l1!K'1!UAob4ryc
61 vg0>!z7t)Y=!g=!=tKDm>!g=!Df==tEm>d!EXz!)fz!=tKDm>_
62 DI{$!o ^wA1!I1!1^95Z$!I1!5V11^(Z$p!(No!wVo!1^95Z$R.
63 q+gi!dhHf)%!+%!%H'&Gi!+%!&F%%HjGi|!jDd!fFd!%H'&GiE<
64 ?lSO!YQ2Upx!lx!x2tv4O!lx!v6xx2M4O)!M:Y!U6Y!x2tv4O8J
66 :0+z!C#e3@`!0`!`ePXmz!0`!Xu``ermzA!r&C!3uC!`ePXmz}f
67 gqv`!8kO"(T!qT!TO>IZ`!qT!IeTTOUZ`M!U{8!"e8!TO>IZ`pt
68 5SbF!-T9poH!SH!H9,:GF!SH!:UHH98GFY!8q-!pU-!H9,:GFc#
69 b5N,!"=#_W<!5<!<#y+4,!5<!+E<<#z4,e!zg"!_E"!<#y+4,V1
71 ]X&W!knV='$!X$!$VUlmW!X$!l%$$V@mW}!@Sk!=%k!$VUlmW<M
72 +:q=!`W@,nw!:w!w@C]Z=!:w!]tww@#Z=*!#I`!,t`!w@C]Z=/[
73 X{]#!U@*zVk!{k!k*1NG#!{k!Ndkk*eG#6!e?U!zdU!k*1NG#"i
74 &]Ih!J)si>_!]_!_s~?4h!]_!?T__sH4hB!H5J!iTJ!_s~?4htw
77 Nbly!)C16U;!b;!;1HqZy!b;!q$;;1PZyf!Pv)!6$)!;1HqZyMB
78 {DX_!},z%=/!D/!/z6bG_!D/!bs//z3G_r!3l}!%s}!/z6bG_@P
79 I&DE!rtds%#!&#!#d$S4E!&#!Sc##du4E~!ubr!scr!#d$S4E3^
81 DI{p!\F8QTj!Ij!j8_5mp!Ij!5Cjj8;mp7!;N\!QC\!j8_5mpxz
82 q+gV!Q/"@<^!+^!^"M&ZV!+^!&3^^"}ZVC!}DQ!@3Q!^"M&ZVk)
83 ?lS<!Fwk/$R!lR!Rk;vG<!lR!v#RRk`G<O!`:F!/#F!Rk;vG<^7
84 lN?"!;`U}kF!NF!FU)g4"!NF!grFFUC4"[!C0;!}r;!FU)g4"QE
86 gqvM!%2)[;.!q.!.)dImM!q.!IR..)hmMs!h{%![R%!.)dImM7a
87 5Sb3!yzrJ#"!S"!"rR:Z3!S"!:B""rKZ3 !Kqy!JBy!"rR:Z3*o
88 b5Nx!nc\9ju!5u!u\@+Gx!5u!+2uu\.Gx,!.gn!92n!u\@+Gx|}
89 0v:^!cLF(Ri!vi!iF.{4^!vi!{"iiFp4^8!p]c!("c!iF.{4^o,
91 +:q*!M}ye"Q!:Q!Qyi]m*!:Q!]aQQy6m*P!6IM!eaM!Qyi]m*UH
92 X{]o!BfcTiE!{E!EcWNZo!{E!NQEEcxZo\!x?B!TQB!EcWNZoHV
93 &]IU!7OMCQ9!]9!9ME?GU!]9!?A99M[GUh![57!CA7!9ME?GU;d
94 S?5;!,8729-!?-!-7304;!?-!01--7>4;t!>+,!21,!-7304;.r
96 Nblf!uijoht!bt!tjnqmf!bt!qpttjcmf-!cvu!opu!tjnqmfs/
97 {DXL!jRT^Ph!Dh!hT\bZL!Dh!b`hhTFZL9!Flj!^`j!hT\bZLf=
98 I&D2!_;>M8\!&\!\>JSG2!&\!SP\\>)G2E!)b_!MP_!\>JSG2YK
99 vg0w!T$(< P!gP!P(8D4w!gP!D@PP(k4wQ!kXT!<@T!P(8D4wLY
 """