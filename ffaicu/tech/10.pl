sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$temp_gold =  int(rand($gold)) + 1;
		$com1 .="<font class=\"yellow\">�����𓐂񂾁􍇌v$temp_gold�f�Q�b�g��</font><br>";
		$gold += $temp_gold;
	}
}
sub atowaza{}
1;