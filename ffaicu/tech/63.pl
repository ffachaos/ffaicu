sub hissatu{}
sub atowaza{
	if ($waza_ritu > int(rand(120))) {
		$dmg1 = $dmg2;
		$sake1 = $sake2;
		$hpplus1 = $hpplus2;
		$clit1 = $clit2;
		if ($hpplus1) {
			$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
		}
		$com1 .= "<font class=\"red\">$mname $winner[3]�̂��̂܂ˁ`��</font><br>";
	}
}
1;