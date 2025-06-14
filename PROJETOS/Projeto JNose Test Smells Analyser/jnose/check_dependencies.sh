echo "Java Installed?"
if [[ $(Java -version 2>&1) == *"Java"* ]]; then echo ok; else echo 'not ok'; fi
echo ""
echo "Jnose needs Java version 11 or higher"
java -version
echo ""
echo "Maven Installed?"
if [[ $(mvn -version 2>&1) == *"Maven"*"3."* ]]; then echo ok; else echo 'not ok'; fi
echo ""
mvn -version