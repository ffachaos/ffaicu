sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		if (int(rand(2))==0) {
			$charadown[7] = int(rand(3));
			$charadown[8] = int(rand(3));
			$charadown[9] = int(rand(3));
			$charadown[10] = int(rand(3));
			$charadown[11] = int(rand(3));
			$charadown[12] = int(rand(3));
			$charadown[13] = int(rand(3));
			$charadown[20] = int(rand(3));
			$chara[7] -= $charadown[7];
			$chara[8] -= $charadown[8];
			$chara[9] -= $charadown[9];
			$chara[10] -= $charadown[10];
			$chara[11] -= $charadown[11];
			$chara[12] -= $charadown[12];
			$chara[13] -= $charadown[13];
			$chara[20] -= $charadown[20];
			$sake1 -= 999999;
			$dmg2 += int(rand($mrand)) * 2;
			$com2 .= <<"EOM";
<font class=\"red\" size=5>�L�����I�I�I</font><br>
<font class =\"white\" size = 2>
�͂�<font class =\"yellow\">$charadown[7]</font>���������B<br>
���͂�<font class =\"yellow\">$charadown[8]</font>���������B<br>
�M�S��<font class =\"yellow\">$charadown[9]</font>���������B<br>
�����͂�<font class =\"yellow\">$charadown[10]</font>���������B<br>
��p����<font class =\"yellow\">$charadown[11]</font>���������B<br>
������<font class =\"yellow\">$charadown[12]</font>���������B<br>
���͂�<font class =\"yellow\">$charadown[13]</font>���������B<br>
�J���}��<font class =\"yellow\">$charadown[20]</font>���������B
</font><br>
EOM
		} else {
			$dmg2 += int(rand($mrand)) * 10;
			$dmg2 += $item[4];
			$com2 .= "<font class=\"red\" size=5>�L�����I�I�I</font><br>";
		}
	}
}
sub mons_atowaza{}
1;