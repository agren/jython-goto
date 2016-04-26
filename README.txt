Jython-goto is an experiment which adds goto-functionality to Jython.
Use it at your own risk.

How it works:
To allow gotos in Jython the Jython compiler has been modified. It works by inserting goto- and label-instructions whenever 'goto .label_name' and 'label .label_name', respectively, are encountered during compilation.
The only modifications made to Jython are in the file 'CodeCompiler.java': https://github.com/agren/jython-goto/commit/29568be768d7851cf87ea25697a03cff1f8e8bf1#diff-0e8b4205a3d7ca7f18530d7a7cd2c8e0

Usage:
An example .py file can be found in the 'jygoto' directory.
Run your .py with the modified Jython version.

Compiling Jython:
Compiling should be as easy as running 'ant' from the base directory.
The modifications made to Jython are tiny. So if there are any problems you should look up how to compile Jython.

The original Jython readme has been renamed to README_jython.txt
