sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dmg1 = ($chara[8] + $chara[9]) * int(rand(100));
		$com1 .= "<font class=\"yellow\" size=5>�֒f���@�A���e�}�I�I</font>";
		if ($waza_ritu > int(rand(80))) {
			$dmg1 += ($chara[9]) * int(rand(80));
			$com1 .= "<font class=\"white\" size=5>�z�[���[�I�I</font>";
		}
		if ($waza_ritu > int(rand(80))) {
			$dmg1 += ($chara[8]) * int(rand(80));
			$com1 .="<font class=\"red\" size=5>�t���A�I�I</font>";
		}
		if ($waza_ritu > int(rand(80))) {
			$dmg1 += ($chara[8]) * int(rand(100));
			$com1 .="<font class=\"red\" size=5>���e�I�I�I</font>";
		}
		$com1 .= "<br>\n";
		$sake2 -= 999999;
	}
}
sub atowaza{}
1;